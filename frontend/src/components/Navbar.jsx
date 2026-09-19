import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { useCart } from '../context/CartContext'
import './Navbar.css'

export default function Navbar() {
  const { seller, buyer, logout, logoutBuyer } = useAuth()
  const { totalItems } = useCart()
  const navigate = useNavigate()

  const handleSellerLogout = () => {
    logout()
    navigate('/')
  }

  const handleBuyerLogout = () => {
    logoutBuyer()
    navigate('/')
  }

  return (
    <nav className="navbar">
      <div className="container navbar-inner">
        {/* Logo */}
        <Link to="/" className="navbar-logo">
          <span className="logo-icon">⚡</span>
          <span className="logo-text">
            cuet<span className="logo-bd">Ebazar</span>
          </span>
        </Link>

        {/* Center tagline */}
        <span className="navbar-tagline">Bangladesh's Electronics Marketplace</span>

        {/* Right actions */}
        <div className="navbar-actions">
          {/* Cart icon */}
          <Link to="/cart" className="cart-nav-btn" id="nav-cart-btn">
            🛒
            {totalItems > 0 && (
              <span className="cart-nav-badge">{totalItems}</span>
            )}
          </Link>

          {/* Buyer section */}
          {buyer ? (
            <>
              <div className="seller-pill buyer-pill">
                <span className="seller-avatar">{buyer.name?.charAt(0).toUpperCase()}</span>
                <span className="seller-name">{buyer.name}</span>
              </div>
              <button onClick={handleBuyerLogout} className="btn btn-secondary btn-sm" id="buyer-logout-btn">
                Logout
              </button>
            </>
          ) : (
            <>
              <Link to="/buyer/login" className="btn btn-outline btn-sm" id="nav-buyer-login">
                Sign In
              </Link>
              <Link to="/buyer/register" className="btn btn-ghost btn-sm" id="nav-buyer-register">
                Register
              </Link>
            </>
          )}

          {/* Seller section */}
          {seller ? (
            <>
              <Link to="/upload" className="btn btn-primary btn-sm">
                + List Product
              </Link>
              <div className="seller-pill">
                <span className="seller-avatar">{seller.name?.charAt(0).toUpperCase()}</span>
                <span className="seller-name">{seller.shop_name || seller.name}</span>
              </div>
              <button onClick={handleSellerLogout} className="btn btn-secondary btn-sm" id="seller-logout-btn">
                Logout
              </button>
            </>
          ) : (
            <Link to="/seller/login" className="btn btn-primary btn-sm" id="nav-seller-login">
              Seller
            </Link>
          )}
        </div>
      </div>
    </nav>
  )
}
