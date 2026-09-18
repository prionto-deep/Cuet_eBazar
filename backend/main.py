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

app = FastAPI(title="Daraz Clone API", version="1.0.0")

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


# ── Auth routes ───────────────────────────────────────────────────────────────

@app.post("/auth/register", response_model=schemas.Token, status_code=status.HTTP_201_CREATED)
def register(seller_data: schemas.SellerRegister, db: Session = Depends(get_db)):
    existing = crud.get_seller_by_email(db, seller_data.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    seller = crud.create_seller(db, seller_data)
    token = auth.create_access_token(data={"sub": str(seller.id)})
    return {"access_token": token, "token_type": "bearer", "seller": seller}


@app.post("/auth/login", response_model=schemas.Token)
def login(credentials: schemas.SellerLogin, db: Session = Depends(get_db)):
    seller = crud.get_seller_by_email(db, credentials.email)
    if not seller or not auth.verify_password(credentials.password, seller.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    if not seller.is_active:
        raise HTTPException(status_code=403, detail="Account is deactivated")
    token = auth.create_access_token(data={"sub": str(seller.id)})
    return {"access_token": token, "token_type": "bearer", "seller": seller}


@app.get("/auth/me", response_model=schemas.SellerOut)
def get_me(current_seller: models.Seller = Depends(auth.get_current_seller)):
    return current_seller


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
    # Handle image upload
    image_url = None
    if image and image.filename:
        ext = Path(image.filename).suffix.lower()
        if ext not in [".jpg", ".jpeg", ".png", ".webp", ".gif"]:
            raise HTTPException(status_code=400, detail="Invalid image format")
        filename = f"{uuid.uuid4()}{ext}"
        file_path = UPLOAD_DIR / filename
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
        image_url = f"/uploads/{filename}"

    product_data = schemas.ProductCreate(
        name=name,
        description=description,
        price_bdt=price_bdt,
        brand=brand,
        stock=stock,
        category_id=category_id,
    )
    return crud.create_product(db, product_data, image_url, current_seller.id)


# ── Health check ──────────────────────────────────────────────────────────────

@app.get("/health")
def health():
    return {"status": "ok", "message": "Daraz Clone API is running"}
