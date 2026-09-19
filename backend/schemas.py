from pydantic import BaseModel, EmailStr
from typing import Optional, List
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


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price_bdt: Optional[float] = None
    brand: Optional[str] = None
    stock: Optional[int] = None
    category_id: Optional[int] = None


class ProductOut(ProductBase):
    id: int
    image_url: Optional[str] = None
    category_id: int
    category: Optional[CategoryOut] = None
    seller_id: Optional[int] = None
    seller_shop_name: Optional[str] = None
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
    is_admin: bool = False
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str
    seller: SellerOut


# ── Buyer Auth ────────────────────────────────────────────────────────────────

class BuyerRegister(BaseModel):
    name: str
    email: str
    password: str


class BuyerLogin(BaseModel):
    email: str
    password: str


class BuyerOut(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class BuyerToken(BaseModel):
    access_token: str
    token_type: str
    buyer: BuyerOut


# ── Order ─────────────────────────────────────────────────────────────────────

class OrderItem(BaseModel):
    product_id: int
    quantity: int


class OrderCreate(BaseModel):
    items: List[OrderItem]


class OrderItemOut(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    unit_price: float
    subtotal: float


class OrderOut(BaseModel):
    order_id: str
    items: List[OrderItemOut]
    total: float
    message: str


# ── Search / Filter ───────────────────────────────────────────────────────────

class ProductsResponse(BaseModel):
    items: list[ProductOut]
    total: int
    page: int
    pages: int
