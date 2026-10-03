import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv
from jose import JWTError, jwt
import bcrypt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import get_db
import models

# Load backend/.env for local development (real env vars take precedence).
load_dotenv(Path(__file__).with_name(".env"))

SECRET_KEY = os.getenv("JWT_SECRET_KEY", "")
if len(SECRET_KEY) < 32:
    raise RuntimeError(
        "JWT_SECRET_KEY must be set to a random string of at least 32 characters. "
        "Generate one with: python -c \"import secrets; print(secrets.token_urlsafe(48))\""
    )
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 24 hours

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
oauth2_scheme_buyer = OAuth2PasswordBearer(tokenUrl="/auth/buyer/login")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


def get_password_hash(password: str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_seller(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> models.Seller:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        seller_id: int = payload.get("sub")
        if seller_id is None or payload.get("role") != "seller":
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    seller = db.query(models.Seller).filter(models.Seller.id == int(seller_id)).first()
    if seller is None or not seller.is_active:
        raise credentials_exception
    return seller


def get_current_buyer(
    token: str = Depends(oauth2_scheme_buyer),
    db: Session = Depends(get_db)
) -> models.Buyer:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate buyer credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        buyer_id: int = payload.get("sub")
        if buyer_id is None or payload.get("role") != "buyer":
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    buyer = db.query(models.Buyer).filter(models.Buyer.id == int(buyer_id)).first()
    if buyer is None or not buyer.is_active:
        raise credentials_exception
    return buyer
