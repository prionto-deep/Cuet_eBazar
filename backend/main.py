import os
import uuid
import shutil
from pathlib import Path
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Form, status, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

import models
import schemas
import crud
import auth
from database import engine, get_db
from seed import seed

# ── Create tables + seed on startup ─────────────────────────────────────────
models.Base.metadata.create_all(bind=engine)
seed()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

app = FastAPI(title="cuetEbazar API", version="2.0.0")

# ── CORS ──────────────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Static files (uploaded images) ───────────────────────────────────────────
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")


# ── Seller Auth routes ────────────────────────────────────────────────────────

@app.post("/auth/register", response_model=schemas.Token, status_code=status.HTTP_201_CREATED)
def register(seller_data: schemas.SellerRegister, db: Session = Depends(get_db)):
    existing = crud.get_seller_by_email(db, seller_data.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    seller = crud.create_seller(db, seller_data)
    token = auth.create_access_token(data={"sub": str(seller.id), "role": "seller"})
    return {"access_token": token, "token_type": "bearer", "seller": seller}


@app.post("/auth/login", response_model=schemas.Token)
def login(credentials: schemas.SellerLogin, db: Session = Depends(get_db)):
    seller = crud.get_seller_by_email(db, credentials.email)
    if not seller or not auth.verify_password(credentials.password, seller.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    if not seller.is_active:
        raise HTTPException(status_code=403, detail="Account is deactivated")
    token = auth.create_access_token(data={"sub": str(seller.id), "role": "seller"})
    return {"access_token": token, "token_type": "bearer", "seller": seller}


@app.get("/auth/me", response_model=schemas.SellerOut)
def get_me(current_seller: models.Seller = Depends(auth.get_current_seller)):
    return current_seller


# ── Buyer Auth routes ─────────────────────────────────────────────────────────

@app.post("/auth/buyer/register", response_model=schemas.BuyerToken, status_code=status.HTTP_201_CREATED)
def buyer_register(buyer_data: schemas.BuyerRegister, db: Session = Depends(get_db)):
    existing = crud.get_buyer_by_email(db, buyer_data.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    buyer = crud.create_buyer(db, buyer_data)
    token = auth.create_access_token(data={"sub": str(buyer.id), "role": "buyer"})
    return {"access_token": token, "token_type": "bearer", "buyer": buyer}


@app.post("/auth/buyer/login", response_model=schemas.BuyerToken)
def buyer_login(credentials: schemas.BuyerLogin, db: Session = Depends(get_db)):
    buyer = crud.get_buyer_by_email(db, credentials.email)
    if not buyer or not auth.verify_password(credentials.password, buyer.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    if not buyer.is_active:
        raise HTTPException(status_code=403, detail="Account is deactivated")
    token = auth.create_access_token(data={"sub": str(buyer.id), "role": "buyer"})
    return {"access_token": token, "token_type": "bearer", "buyer": buyer}


@app.get("/auth/buyer/me", response_model=schemas.BuyerOut)
def get_buyer_me(current_buyer: models.Buyer = Depends(auth.get_current_buyer)):
    return current_buyer


# ── Category routes ───────────────────────────────────────────────────────────

@app.get("/categories", response_model=list[schemas.CategoryOut])
def list_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)


# ── Product routes ────────────────────────────────────────────────────────────

@app.get("/products", response_model=schemas.ProductsResponse)
def list_products(
    search: Optional[str] = Query(None),
    category: Optional[str] = Query(None, description="Category slug"),
    min_price: Optional[float] = Query(None, ge=0),
    max_price: Optional[float] = Query(None, ge=0),
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return crud.get_products(
        db,
        search=search,
        category_slug=category,
        min_price=min_price,
        max_price=max_price,
        page=page,
        limit=limit,
    )


@app.get("/products/{product_id}", response_model=schemas.ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.post("/products", response_model=schemas.ProductOut, status_code=status.HTTP_201_CREATED)
async def create_product(
    name: str = Form(...),
    description: str = Form(""),
    price_bdt: float = Form(...),
    brand: str = Form(""),
    stock: int = Form(0),
    category_id: int = Form(...),
    image: Optional[UploadFile] = File(None),
    current_seller: models.Seller = Depends(auth.get_current_seller),
    db: Session = Depends(get_db),
):
    image_url = _save_image(image)
    product_data = schemas.ProductCreate(
        name=name,
        description=description,
        price_bdt=price_bdt,
        brand=brand,
        stock=stock,
        category_id=category_id,
    )
    return crud.create_product(db, product_data, image_url, current_seller.id)


@app.put("/products/{product_id}", response_model=schemas.ProductOut)
async def update_product(
    product_id: int,
    name: Optional[str] = Form(None),
    description: Optional[str] = Form(None),
    price_bdt: Optional[float] = Form(None),
    brand: Optional[str] = Form(None),
    stock: Optional[int] = Form(None),
    category_id: Optional[int] = Form(None),
    image: Optional[UploadFile] = File(None),
    current_seller: models.Seller = Depends(auth.get_current_seller),
    db: Session = Depends(get_db),
):
    image_url = _save_image(image)
    update_data = schemas.ProductUpdate(
        name=name,
        description=description,
        price_bdt=price_bdt,
        brand=brand,
        stock=stock,
        category_id=category_id,
    )
    product = crud.update_product(db, product_id, current_seller.id, update_data, image_url, is_admin=current_seller.is_admin)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found or not owned by you")
    return product


@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(
    product_id: int,
    current_seller: models.Seller = Depends(auth.get_current_seller),
    db: Session = Depends(get_db),
):
    success = crud.delete_product(db, product_id, current_seller.id, is_admin=current_seller.is_admin)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found or not owned by you")


# ── Order routes ──────────────────────────────────────────────────────────────

@app.post("/orders", response_model=schemas.OrderOut, status_code=status.HTTP_201_CREATED)
def place_order(
    order_data: schemas.OrderCreate,
    current_buyer: models.Buyer = Depends(auth.get_current_buyer),
    db: Session = Depends(get_db),
):
    try:
        return crud.place_order(db, current_buyer.id, order_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# ── Health check ──────────────────────────────────────────────────────────────

@app.get("/health")
def health():
    return {"status": "ok", "message": "cuetEbazar API is running"}


# ── Helpers ───────────────────────────────────────────────────────────────────

def _save_image(image: Optional[UploadFile]) -> Optional[str]:
    if not image or not image.filename:
        return None
    ext = Path(image.filename).suffix.lower()
    if ext not in [".jpg", ".jpeg", ".png", ".webp", ".gif"]:
        raise HTTPException(status_code=400, detail="Invalid image format")
    filename = f"{uuid.uuid4()}{ext}"
    file_path = UPLOAD_DIR / filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    return f"/uploads/{filename}"
