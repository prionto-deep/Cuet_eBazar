<div align="center">

# ⚡ PrionyxOnline

### Bangladesh's Premier Electronics Marketplace

**A full-stack e-commerce platform** built with FastAPI, React, and SQLite — inspired by Daraz.com.bd

[![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18.2+-61DAFB?style=flat-square&logo=react&logoColor=black)](https://react.dev)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=flat-square&logo=sqlite&logoColor=white)](https://sqlite.org)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Node.js](https://img.shields.io/badge/Node.js-18+-339933?style=flat-square&logo=node.js&logoColor=white)](https://nodejs.org)

</div>

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Getting Started](#-getting-started)
  - [Backend Setup](#-backend-setup)
  - [Frontend Setup](#-frontend-setup)
- [Backend Reference](#-backend-reference)
  - [API Endpoints](#api-endpoints)
  - [Database Models](#database-models)
  - [Authentication](#authentication)
  - [Environment Variables](#environment-variables)
- [Frontend Reference](#-frontend-reference)
  - [Pages](#pages)
  - [Components](#components)
  - [API Client & Currency](#api-client--currency)
  - [State Management](#state-management)
- [Product Categories](#-product-categories)
- [Running in Production](#-running-in-production)
- [Troubleshooting](#-troubleshooting)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 **Smart Search** | Full-text search across product name, brand, and description |
| 💰 **Budget Filter** | Min/max price filter with quick preset buttons |
| 💱 **Dual Currency** | Every product shows BDT (৳) primary + USD ($) equivalent |
| 📁 **5 Categories** | Smartphones, Laptops, Headphones, Smart TVs, Cameras |
| 📦 **50 Mock Products** | 10 realistic products per category, seeded automatically |
| 📤 **Product Upload** | Sellers can list new products with image upload |
| 🔐 **Seller Auth** | JWT-based registration/login with bcrypt password hashing |
| 🛡️ **Protected Routes** | Upload page requires seller login — auto-redirect if not authenticated |
| 📱 **Responsive UI** | Works on mobile, tablet, and desktop |
| ⚡ **Premium Dark Design** | Glassmorphism, gradient orbs, hover animations, skeleton loaders |
| 📄 **Pagination** | Server-side pagination with page controls |
| 🖼️ **Image Serving** | Uploaded images served as static files via FastAPI |

---

## 🛠 Tech Stack

### Backend
| Technology | Version | Purpose |
|---|---|---|
| **FastAPI** | ≥ 0.111 | REST API framework |
| **SQLAlchemy** | ≥ 2.0 | ORM for SQLite |
| **SQLite** | Built-in | Lightweight file-based database |
| **Pydantic** | v2 | Request/response validation |
| **python-jose** | ≥ 3.3 | JWT token creation & verification |
| **bcrypt** | ≥ 4.1 | Password hashing |
| **uvicorn** | ≥ 0.29 | ASGI server |
| **python-multipart** | ≥ 0.0.9 | Multipart form (image upload) |
| **aiofiles** | ≥ 23.2 | Async file I/O |

### Frontend
| Technology | Version | Purpose |
|---|---|---|
| **React** | 18.2 | UI component library |
| **Vite** | 5.x | Build tool & dev server |
| **React Router DOM** | 6.x | Client-side routing |
| **Axios** | 1.6 | HTTP client with JWT interceptor |
| **Vanilla CSS** | — | Custom design system (no Tailwind) |
| **Google Fonts** | Inter | Typography |

---

## 📁 Project Structure

```
excited-meitner/
│
├── backend/                        # FastAPI application
│   ├── main.py                     # App entry point, all route definitions
│   ├── database.py                 # SQLite connection & session factory
│   ├── models.py                   # SQLAlchemy ORM models (Category, Product, Seller)
│   ├── schemas.py                  # Pydantic request/response schemas
│   ├── crud.py                     # Database CRUD operations
│   ├── auth.py                     # JWT helpers, bcrypt password hashing
│   ├── seed.py                     # Mock data seeder (5 categories, 50 products)
│   ├── requirements.txt            # Python dependencies
│   ├── daraz_clone.db              # SQLite database file (auto-created)
│   └── uploads/                    # Uploaded product images (auto-created)
│
├── frontend/                       # React application
│   ├── index.html                  # HTML entry point (Google Fonts loaded here)
│   ├── vite.config.js              # Vite config with backend proxy
│   ├── package.json
│   └── src/
│       ├── main.jsx                # React DOM entry point
│       ├── App.jsx                 # Root app: Router, AuthProvider, Footer
│       ├── App.css                 # App shell & footer styles
│       ├── index.css               # Global design system (tokens, buttons, forms)
│       │
│       ├── api/
│       │   └── client.js           # Axios instance, BDT/USD formatters, all API calls
│       │
│       ├── context/
│       │   └── AuthContext.jsx     # Seller auth state (login, logout, JWT persistence)
│       │
│       ├── components/
│       │   ├── Navbar.jsx          # Top navigation bar with seller menu
│       │   ├── Navbar.css
│       │   ├── SearchBar.jsx       # Text search + budget filter + quick presets
│       │   ├── SearchBar.css
│       │   ├── CategoryNav.jsx     # Horizontal scrollable category pill chips
│       │   ├── CategoryNav.css
│       │   ├── ProductCard.jsx     # Product preview card (image, price, rating)
│       │   ├── ProductCard.css
│       │   ├── ProductGrid.jsx     # Responsive grid with skeleton & pagination
│       │   ├── ProductGrid.css
│       │   └── ProtectedRoute.jsx  # Auth guard — redirects to /seller/login
│       │
│       └── pages/
│           ├── Home.jsx            # Main marketplace: hero, search, categories, grid
│           ├── Home.css
│           ├── ProductDetail.jsx   # Full product detail view
│           ├── ProductDetail.css
│           ├── UploadProduct.jsx   # Seller product listing form (protected)
│           ├── UploadProduct.css
│           ├── SellerLogin.jsx     # Seller login form
│           ├── SellerRegister.jsx  # Seller registration form
│           └── AuthPages.css       # Shared styles for auth pages
│
├── setup.sh                        # One-command setup script
└── README.md                       # This file
```

---

## ⚙️ Prerequisites

Before you begin, ensure you have the following installed:

| Tool | Minimum Version | Check Command | Install |
|---|---|---|---|
| **Python** | 3.9+ | `python3 --version` | [python.org](https://python.org/downloads) |
| **Node.js** | 18+ | `node --version` | [nodejs.org](https://nodejs.org) |
| **npm** | 9+ | `npm --version` | Bundled with Node.js |

> **Note:** If you don't have Node.js, you can install it via [nvm](https://github.com/nvm-sh/nvm):
> ```bash
> curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
> source ~/.zshrc  # or ~/.bashrc
> nvm install 20 && nvm use 20
> ```

---

## 🚀 Getting Started

### One-Command Setup (Recommended)

```bash
bash setup.sh
```

Or follow the manual steps below:

---

### 🐍 Backend Setup

```bash
# 1. Navigate to the backend folder
cd backend

# 2. Create a Python virtual environment
python3 -m venv venv

# 3. Activate the virtual environment
source venv/bin/activate        # macOS/Linux
# venv\Scripts\activate         # Windows

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create the uploads directory
mkdir -p uploads

# 6. (Optional) Seed the database manually
#    The server seeds automatically on first start, but you can run this explicitly:
python seed.py

# 7. Start the development server
uvicorn main:app --reload --port 8000
```

✅ The backend will be available at: **http://localhost:8000**
📘 Interactive API docs: **http://localhost:8000/docs**

---

### ⚛️ Frontend Setup

Open a **new terminal** and run:

```bash
# 1. Navigate to the frontend folder
cd frontend

# 2. Install npm dependencies
npm install

# 3. Start the Vite dev server
npm run dev
```

✅ The frontend will be available at: **http://localhost:5173**

> The Vite dev server proxies `/api/*` requests to the FastAPI backend at port 8000 automatically.

---

## 📡 Backend Reference

### API Endpoints

#### 🔐 Authentication

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| `POST` | `/auth/register` | No | Register a new seller account |
| `POST` | `/auth/login` | No | Login and receive a JWT token |
| `GET` | `/auth/me` | **Yes (JWT)** | Get current logged-in seller info |

**Register Request Body:**
```json
{
  "name": "John Doe",
  "email": "seller@example.com",
  "password": "mypassword",
  "shop_name": "John's Tech Store"
}
```

**Login Request Body:**
```json
{
  "email": "seller@example.com",
  "password": "mypassword"
}
```

**Token Response:**
```json
{
  "access_token": "eyJhbGci...",
  "token_type": "bearer",
  "seller": {
    "id": 1,
    "name": "John Doe",
    "email": "seller@example.com",
    "shop_name": "John's Tech Store",
    "is_active": true,
    "created_at": "2024-01-01T00:00:00Z"
  }
}
```

---

#### 📂 Categories

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| `GET` | `/categories` | No | List all product categories |

**Response:**
```json
[
  { "id": 1, "name": "Smartphones", "slug": "smartphones", "icon": "📱", "description": "..." },
  { "id": 2, "name": "Laptops",     "slug": "laptops",     "icon": "💻", "description": "..." }
]
```

---

#### 📦 Products

| Method | Endpoint | Auth Required | Description |
|---|---|---|---|
| `GET` | `/products` | No | List/search products with filters |
| `GET` | `/products/{id}` | No | Get a single product by ID |
| `POST` | `/products` | **Yes (JWT)** | Upload a new product |

**GET `/products` — Query Parameters:**

| Parameter | Type | Description | Example |
|---|---|---|---|
| `search` | `string` | Text search (name, brand, description) | `?search=samsung` |
| `category` | `string` | Category slug | `?category=smartphones` |
| `min_price` | `float` | Minimum price in BDT | `?min_price=10000` |
| `max_price` | `float` | Maximum price in BDT | `?max_price=50000` |
| `page` | `int` | Page number (default: 1) | `?page=2` |
| `limit` | `int` | Results per page (default: 20, max: 100) | `?limit=10` |

**Example Requests:**
```bash
# Search for Sony products
curl "http://localhost:8000/products?search=sony"

# Filter laptops under ৳120,000
curl "http://localhost:8000/products?category=laptops&max_price=120000"

# Budget range ৳10,000 to ৳30,000
curl "http://localhost:8000/products?min_price=10000&max_price=30000"
```

**POST `/products` — Upload a Product (multipart/form-data):**

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | ✅ | Product name |
| `description` | string | No | Product description |
| `price_bdt` | float | ✅ | Price in Bangladeshi Taka |
| `brand` | string | No | Brand name |
| `stock` | int | No | Available stock quantity |
| `category_id` | int | ✅ | Category ID |
| `image` | file | No | Product image (JPG, PNG, WEBP, max 10MB) |

```bash
# Example with curl
curl -X POST http://localhost:8000/products \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -F "name=My Product" \
  -F "price_bdt=25000" \
  -F "category_id=1" \
  -F "brand=Samsung" \
  -F "stock=50" \
  -F "image=@/path/to/photo.jpg"
```

---

#### 🖼️ Static Files

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/uploads/{filename}` | Serve uploaded product images |
| `GET` | `/health` | API health check |

---

### Database Models

#### `Category`
| Column | Type | Description |
|---|---|---|
| `id` | Integer (PK) | Auto-increment ID |
| `name` | String | Category name (e.g. "Smartphones") |
| `slug` | String | URL-safe identifier (e.g. "smartphones") |
| `icon` | String | Emoji icon (e.g. "📱") |
| `description` | Text | Category description |

#### `Product`
| Column | Type | Description |
|---|---|---|
| `id` | Integer (PK) | Auto-increment ID |
| `name` | String | Product name |
| `description` | Text | Full product description |
| `price_bdt` | Float | Price in Bangladeshi Taka (BDT) |
| `brand` | String | Brand name |
| `stock` | Integer | Available units |
| `rating` | Float | Average rating (0–5) |
| `review_count` | Integer | Total number of reviews |
| `image_url` | String | URL to product image |
| `category_id` | FK → Category | Associated category |
| `seller_id` | FK → Seller | Seller who listed it |
| `is_active` | Boolean | Whether product is visible |
| `created_at` | DateTime | Listing timestamp |

#### `Seller`
| Column | Type | Description |
|---|---|---|
| `id` | Integer (PK) | Auto-increment ID |
| `name` | String | Seller's full name |
| `email` | String (unique) | Login email |
| `hashed_password` | String | bcrypt-hashed password |
| `shop_name` | String | Optional shop/store name |
| `is_active` | Boolean | Whether account is active |
| `created_at` | DateTime | Registration timestamp |

---

### Authentication

The API uses **JWT (JSON Web Tokens)** for stateless seller authentication.

- Tokens are signed with `HS256` and expire after **24 hours**
- Passwords are hashed with **bcrypt** (cost factor 12)
- Include the token in the `Authorization` header for protected routes:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

### Environment Variables

The following constants are defined in [`auth.py`](backend/auth.py). **Change these before deploying to production:**

| Variable | Default | Description |
|---|---|---|
| `SECRET_KEY` | `"daraz-clone-super-secret-key..."` | JWT signing secret — **must be changed in production** |
| `ALGORITHM` | `"HS256"` | JWT signing algorithm |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `1440` (24h) | Token expiration time |

---

## ⚛️ Frontend Reference

### Pages

| Route | File | Auth | Description |
|---|---|---|---|
| `/` | `Home.jsx` | No | Main marketplace: hero, search, categories, product grid |
| `/products/:id` | `ProductDetail.jsx` | No | Full product detail view |
| `/seller/login` | `SellerLogin.jsx` | No | Seller sign-in page |
| `/seller/register` | `SellerRegister.jsx` | No | Seller registration page |
| `/upload` | `UploadProduct.jsx` | **Yes** | List a new product (protected) |
| `*` | (inline) | No | 404 not found page |

---

### Components

#### `<Navbar />`
- Sticky top bar with glassmorphism effect
- Shows seller name + shop pill when logged in
- Shows "Seller Login" and "Start Selling" buttons when logged out
- "+ List Product" button when authenticated

#### `<SearchBar onSearch={fn} />`
- Full-text search input
- "💰 Budget" toggle reveals min/max price inputs with BDT/USD hints
- Quick preset buttons: Under ৳10K, ৳10K–50K, ৳50K–150K, Above ৳150K
- Calls `onSearch({ search, min_price, max_price })` on submit

#### `<CategoryNav activeSlug={slug} onChange={fn} />`
- Horizontally scrollable pill chips for each category
- "All" chip at the start (empty slug)
- Active state with orange glow border

#### `<ProductCard product={product} />`
- Linked card navigating to `/products/:id`
- Displays: image, brand, name, star rating, review count
- **Price:** `৳139,999` (primary) + `~$1,272` (secondary)
- Stock status badge
- "Add to Cart" button (UI only — no cart backend)

#### `<ProductGrid products={[...]} loading={bool} ... />`
- Responsive CSS grid (auto-fill, min 220px columns)
- Shows 12 skeleton cards while loading
- Empty state with icon when no results
- Pagination controls at the bottom

#### `<ProtectedRoute />`
- Wraps the `/upload` route
- If seller is not authenticated → redirects to `/seller/login`
- Passes `state={{ from: '/upload' }}` so the user is redirected back after login

---

### API Client & Currency

All API calls are in [`src/api/client.js`](frontend/src/api/client.js):

```js
import { fetchProducts, fetchProduct, createProduct,
         loginSeller, registerSeller, fetchCategories } from './api/client'
```

**Currency helpers (1 USD = 110 BDT):**

```js
import { formatBDT, formatUSD } from './api/client'

formatBDT(139999)   // → "৳1,39,999"
formatUSD(139999)   // → "$1272.72"
```

**JWT is automatically attached** to every request via an Axios interceptor — no manual token handling needed in components.

---

### State Management

Authentication state is managed via React Context:

```jsx
import { useAuth } from './context/AuthContext'

const { seller, loading, login, logout } = useAuth()

// seller — null if not logged in, or { id, name, email, shop_name }
// login(token, sellerData) — stores JWT in localStorage, updates state
// logout() — clears localStorage, resets state
```

---

## 🗂️ Product Categories

50 mock products are pre-loaded in the database across 5 categories:

### 📱 Smartphones (10 products)
Samsung Galaxy S24 Ultra, Apple iPhone 15 Pro Max, Xiaomi 14 Pro, OnePlus 12, Google Pixel 8 Pro, Samsung Galaxy A54 5G, Realme GT 5 Pro, Vivo X100 Pro, OPPO Find X7 Ultra, Motorola Edge 40 Pro

### 💻 Laptops (10 products)
Apple MacBook Air M3, Dell XPS 15 9530, Lenovo ThinkPad X1 Carbon, HP Spectre x360 14, ASUS ROG Zephyrus G14, Microsoft Surface Laptop 5, Acer Swift X 14, LG Gram 16, Razer Blade 15, Lenovo IdeaPad Slim 5

### 🎧 Headphones (10 products)
Sony WH-1000XM5, Apple AirPods Pro 2nd Gen, Bose QuietComfort 45, Sennheiser Momentum 4, JBL Tune 760NC, Jabra Evolve2 85, Samsung Galaxy Buds2 Pro, Sony WF-1000XM5, Anker Soundcore Q45, Beyerdynamic DT 770 Pro

### 📺 Smart TVs (10 products)
Samsung 65" QLED Q80C, LG C3 OLED 55", Sony Bravia XR A80L, TCL 55" C835 Mini LED, Hisense 65" U8K, Samsung 75" Crystal UHD, LG 43" UHD UR80, Xiaomi TV S Pro 65", OnePlus TV Y1S Pro, Vizio 50" M-Series

### 📷 Cameras (10 products)
Canon EOS R6 Mark II, Sony Alpha A7 IV, Nikon Z8, Fujifilm X-T5, GoPro HERO12 Black, Canon EOS R50, Sony ZV-E10 II, DJI Osmo Pocket 3, Nikon Z30, Panasonic Lumix G100D

---

## 🏭 Running in Production

### Backend

```bash
# Use gunicorn with uvicorn workers
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

**Before going live:**
1. Change `SECRET_KEY` in `auth.py` to a strong random string:
   ```bash
   python3 -c "import secrets; print(secrets.token_hex(32))"
   ```
2. Update CORS origins in `main.py` to your production domain
3. Use a proper database (PostgreSQL) instead of SQLite for multi-user production

### Frontend

```bash
# Build for production
npm run build

# Preview the build locally
npm run preview
```

The built files will be in `frontend/dist/`. Serve them with Nginx, Vercel, or any static host.

---

## 🔧 Troubleshooting

### `npm` or `node` not found
```bash
# Install via nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
source ~/.zshrc
nvm install 20 && nvm use 20
```

### `pip install` fails (Python 3.14 compatibility)
If you see errors with `passlib` or `pillow`, these packages have known issues on Python 3.14. The project already uses `bcrypt` directly to avoid this.

### Backend returns `500 Internal Server Error` on auth
Ensure `bcrypt` (not `passlib`) is installed:
```bash
source venv/bin/activate
pip install bcrypt
```

### Frontend shows no products (CORS error)
Make sure the backend is running on port `8000` before starting the frontend. Check the browser console for CORS errors — update the `allow_origins` list in `main.py` if needed.

### Products not loading after restart
The database (`daraz_clone.db`) is persistent. If you delete it, the seeder will automatically re-populate on the next backend start.

---

## 📜 License

This project is for educational and personal use.

---

<div align="center">

Built with ❤️ using **FastAPI + React + SQLite** · PrionyxOnline 2024

</div>
