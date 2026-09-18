import math
from typing import Optional
from sqlalchemy.orm import Session
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

def get_products(
    db: Session,
    search: Optional[str] = None,
    category_slug: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    page: int = 1,
    limit: int = 20,
):
    query = db.query(models.Product).filter(models.Product.is_active == True)

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

    return {"items": items, "total": total, "page": page, "pages": pages}


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(
        models.Product.id == product_id,
        models.Product.is_active == True
    ).first()


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
    return db_product


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
