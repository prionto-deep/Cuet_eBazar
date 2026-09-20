import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import { AuthProvider } from './context/AuthContext'
import { CartProvider } from './context/CartContext'
import Navbar from './components/Navbar'
import ProtectedRoute from './components/ProtectedRoute'
import Home from './pages/Home'
import ProductDetail from './pages/ProductDetail'
import UploadProduct from './pages/UploadProduct'
import AdminDashboard from './pages/AdminDashboard'
import SellerLogin from './pages/SellerLogin'
import SellerRegister from './pages/SellerRegister'
import BuyerLogin from './pages/BuyerLogin'
import BuyerRegister from './pages/BuyerRegister'
import Cart from './pages/Cart'
import './App.css'

function Footer() {
  return (
    <footer className="footer">
      <div className="container footer-inner">
        <div className="footer-brand">
          <span className="logo-icon">⚡</span>
          <span style={{ fontWeight: 800, fontSize: '1.1rem' }}>
            cuet<span style={{ color: 'var(--brand-orange)' }}>Ebazar</span>
          </span>
          <p className="footer-tagline">Bangladesh's Electronics Marketplace</p>
        </div>
        <div className="footer-links">
          <div className="footer-col">
            <h4 className="footer-col-title">Categories</h4>
            {['Smartphones', 'Laptops', 'Headphones', 'Smart TVs', 'Cameras'].map(c => (
              <Link key={c} to="/" className="footer-link">{c}</Link>
            ))}
          </div>
          <div className="footer-col">
            <h4 className="footer-col-title">Buyer</h4>
            <Link to="/buyer/register" className="footer-link">Create Account</Link>
            <Link to="/buyer/login" className="footer-link">Sign In</Link>
            <Link to="/cart" className="footer-link">🛒 View Cart</Link>
          </div>
          <div className="footer-col">
            <h4 className="footer-col-title">Seller</h4>
            <Link to="/seller/register" className="footer-link">Start Selling</Link>
            <Link to="/seller/login" className="footer-link">Seller Login</Link>
            <Link to="/upload" className="footer-link">List a Product</Link>
          </div>
          <div className="footer-col">
            <h4 className="footer-col-title">Currency</h4>
            <span className="footer-text">BDT (৳) — Primary</span>
            <span className="footer-text">USD ($) — Secondary</span>
            <span className="footer-text">Rate: 1 USD = ৳110</span>
          </div>
        </div>
      </div>
      <div className="footer-bottom">
        <p>© 2024 cuetEbazar. Built with FastAPI + React + SQLite.</p>
      </div>
    </footer>
  )
}

export default function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <CartProvider>
          <div className="app-shell">
            <Navbar />
            <main className="app-main">
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/products/:id" element={<ProductDetail />} />
                <Route path="/cart" element={<Cart />} />
                <Route path="/buyer/login" element={<BuyerLogin />} />
                <Route path="/buyer/register" element={<BuyerRegister />} />
                <Route path="/seller/login" element={<SellerLogin />} />
                <Route path="/seller/register" element={<SellerRegister />} />
                <Route
                  path="/upload"
                  element={
                    <ProtectedRoute>
                      <UploadProduct />
                    </ProtectedRoute>
                  }
                />
                <Route
                  path="/admin"
                  element={
                    <ProtectedRoute>
                      <AdminDashboard />
                    </ProtectedRoute>
                  }
                />
                {/* 404 */}
                <Route path="*" element={
                  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', minHeight: '60vh', gap: '1rem' }}>
                    <div style={{ fontSize: '5rem' }}>404</div>
                    <h2 style={{ color: 'var(--text-primary)', fontSize: '1.5rem' }}>Page not found</h2>
                    <Link to="/" className="btn btn-primary">← Go Home</Link>
                  </div>
                } />
              </Routes>
            </main>
            <Footer />
          </div>
        </CartProvider>
      </AuthProvider>
    </BrowserRouter>
  )
}
