import math
import uuid
from typing import Optional, List
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import or_
import models
import schemas
import auth


# ── Categories ────────────────────────────────────────────────────────────────

def get_categories(db: Session):
    return db.query(models.Category).all()


def get_category_by_slug(db: Session, slug: str):
    return db.query(models.Category).filter(models.Category.slug == slug).first()


# ── Products ──────────────────────────────────────────────────────────────────

def _enrich_product(product: models.Product) -> models.Product:
    """Attach seller_shop_name as a dynamic attribute for serialisation."""
    if product and product.seller:
        product.seller_shop_name = product.seller.shop_name or product.seller.name
    else:
        product.seller_shop_name = None
    return product


def get_products(
    db: Session,
    search: Optional[str] = None,
    category_slug: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    page: int = 1,
    limit: int = 20,
):
    query = (
        db.query(models.Product)
        .options(joinedload(models.Product.seller), joinedload(models.Product.category))
        .filter(models.Product.is_active == True)
    )

    if search:
        search_term = f"%{search}%"
        query = query.filter(
            or_(
                models.Product.name.ilike(search_term),
                models.Product.description.ilike(search_term),
                models.Product.brand.ilike(search_term),
            )
        )

    if category_slug:
        category = get_category_by_slug(db, category_slug)
        if category:
            query = query.filter(models.Product.category_id == category.id)

    if min_price is not None:
        query = query.filter(models.Product.price_bdt >= min_price)

    if max_price is not None:
        query = query.filter(models.Product.price_bdt <= max_price)

    total = query.count()
    skip = (page - 1) * limit
    items = query.order_by(models.Product.created_at.desc()).offset(skip).limit(limit).all()
    pages = math.ceil(total / limit) if total > 0 else 1

    enriched = [_enrich_product(p) for p in items]
    return {"items": enriched, "total": total, "page": page, "pages": pages}


def get_product(db: Session, product_id: int):
    product = (
        db.query(models.Product)
        .options(joinedload(models.Product.seller), joinedload(models.Product.category))
        .filter(models.Product.id == product_id, models.Product.is_active == True)
        .first()
    )
    return _enrich_product(product) if product else None


def create_product(
    db: Session,
    product_data: schemas.ProductCreate,
    image_url: Optional[str],
    seller_id: int,
):
    db_product = models.Product(
        **product_data.model_dump(),
        image_url=image_url,
        seller_id=seller_id,
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return get_product(db, db_product.id)


def update_product(
    db: Session,
    product_id: int,
    seller_id: int,
    data: schemas.ProductUpdate,
    image_url: Optional[str] = None,
    is_admin: bool = False,
):
    query = db.query(models.Product).filter(
        models.Product.id == product_id,
        models.Product.is_active == True,
    )
    if not is_admin:
        query = query.filter(models.Product.seller_id == seller_id)
    product = query.first()
    if not product:
        return None

    update_data = data.model_dump(exclude_unset=True, exclude_none=True)
    for field, value in update_data.items():
        setattr(product, field, value)
    if image_url is not None:
        product.image_url = image_url

    db.commit()
    db.refresh(product)
    return get_product(db, product.id)


def delete_product(db: Session, product_id: int, seller_id: int, is_admin: bool = False) -> bool:
    query = db.query(models.Product).filter(
        models.Product.id == product_id,
        models.Product.is_active == True,
    )
    if not is_admin:
        query = query.filter(models.Product.seller_id == seller_id)
    product = query.first()
    if not product:
        return False
    product.is_active = False
    db.commit()
    return True


# ── Sellers ───────────────────────────────────────────────────────────────────

def get_seller_by_email(db: Session, email: str):
    return db.query(models.Seller).filter(models.Seller.email == email).first()


def create_seller(db: Session, seller_data: schemas.SellerRegister):
    hashed_pw = auth.get_password_hash(seller_data.password)
    db_seller = models.Seller(
        name=seller_data.name,
        email=seller_data.email,
        hashed_password=hashed_pw,
        shop_name=seller_data.shop_name,
    )
    db.add(db_seller)
    db.commit()
    db.refresh(db_seller)
    return db_seller


# ── Buyers ────────────────────────────────────────────────────────────────────

def get_buyer_by_email(db: Session, email: str):
    return db.query(models.Buyer).filter(models.Buyer.email == email).first()


def create_buyer(db: Session, buyer_data: schemas.BuyerRegister):
    hashed_pw = auth.get_password_hash(buyer_data.password)
    db_buyer = models.Buyer(
        name=buyer_data.name,
        email=buyer_data.email,
        hashed_password=hashed_pw,
    )
    db.add(db_buyer)
    db.commit()
    db.refresh(db_buyer)
    return db_buyer


# ── Orders ────────────────────────────────────────────────────────────────────

def place_order(db: Session, buyer_id: int, order_data: schemas.OrderCreate):
    """
    Atomically decrement stock for each item and return an order summary.
    Raises ValueError with a message if any item has insufficient stock.
    """
    order_items_out = []
    total = 0.0

    if not order_data.items:
        raise ValueError("Order must contain at least one item.")

    for item in order_data.items:
        if item.quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        product = db.query(models.Product).filter(
            models.Product.id == item.product_id,
            models.Product.is_active == True,
        ).with_for_update().first()

        if not product:
            raise ValueError(f"Product ID {item.product_id} not found.")
        if product.stock < item.quantity:
            raise ValueError(
                f"Not enough stock for '{product.name}'. "
                f"Available: {product.stock}, requested: {item.quantity}."
            )

        product.stock -= item.quantity
        subtotal = product.price_bdt * item.quantity
        total += subtotal

        order_items_out.append(schemas.OrderItemOut(
            product_id=product.id,
            product_name=product.name,
            quantity=item.quantity,
            unit_price=product.price_bdt,
            subtotal=subtotal,
        ))

    db.commit()

    return schemas.OrderOut(
        order_id=str(uuid.uuid4())[:8].upper(),
        items=order_items_out,
        total=total,
        message="Order placed successfully! Thank you for shopping at cuetEbazar.",
    )
