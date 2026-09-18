import { Link, useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import './Navbar.css'

export default function Navbar() {
  const { seller, logout } = useAuth()
  const navigate = useNavigate()

  const handleLogout = () => {
    logout()
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
          {seller ? (
            <>
              <Link to="/upload" className="btn btn-primary btn-sm">
                + List Product
              </Link>
              <div className="seller-pill">
                <span className="seller-avatar">{seller.name?.charAt(0).toUpperCase()}</span>
                <span className="seller-name">{seller.shop_name || seller.name}</span>
              </div>
              <button onClick={handleLogout} className="btn btn-secondary btn-sm">
                Logout
              </button>
            </>
          ) : (
            <>
              <Link to="/seller/login" className="btn btn-outline btn-sm">
                Seller Login
              </Link>
              <Link to="/seller/register" className="btn btn-primary btn-sm">
                Start Selling
              </Link>
            </>
          )}
        </div>
      </div>
    </nav>
  )
}
