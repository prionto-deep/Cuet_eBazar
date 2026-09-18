from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# ── Category ─────────────────────────────────────────────────────────────────

class CategoryBase(BaseModel):
    name: str
    slug: str
    icon: str
    description: Optional[str] = None


class CategoryOut(CategoryBase):
    id: int
    class Config:
        from_attributes = True


# ── Product ──────────────────────────────────────────────────────────────────

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price_bdt: float
    brand: Optional[str] = None
    stock: int = 0
    rating: float = 0.0
    review_count: int = 0


class ProductCreate(ProductBase):
    category_id: int


class ProductOut(ProductBase):
    id: int
    image_url: Optional[str] = None
    category_id: int
    category: Optional[CategoryOut] = None
    seller_id: Optional[int] = None
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


# ── Seller Auth ───────────────────────────────────────────────────────────────

class SellerRegister(BaseModel):
    name: str
    email: str
    password: str
    shop_name: Optional[str] = None


class SellerLogin(BaseModel):
    email: str
    password: str


class SellerOut(BaseModel):
    id: int
    name: str
    email: str
    shop_name: Optional[str] = None
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str
    seller: SellerOut


# ── Search / Filter ───────────────────────────────────────────────────────────

class ProductsResponse(BaseModel):
    items: list[ProductOut]
    total: int
    page: int
    pages: int
