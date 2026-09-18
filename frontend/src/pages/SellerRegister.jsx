import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { registerSeller } from '../api/client'
import { useAuth } from '../context/AuthContext'
import './AuthPages.css'

export default function SellerRegister() {
  const { login } = useAuth()
  const navigate = useNavigate()
  const [form, setForm] = useState({ name: '', email: '', shop_name: '', password: '', confirm_password: '' })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleChange = (e) => {
    setForm((f) => ({ ...f, [e.target.name]: e.target.value }))
    setError(null)
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (form.password !== form.confirm_password) {
      return setError('Passwords do not match')
    }
    if (form.password.length < 6) {
      return setError('Password must be at least 6 characters')
    }
    setLoading(true)
    setError(null)
    try {
      const data = await registerSeller({
        name: form.name,
        email: form.email,
        shop_name: form.shop_name,
        password: form.password,
      })
      login(data.access_token, data.seller)
      navigate('/upload')
    } catch (err) {
      setError(err.response?.data?.detail || 'Registration failed. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="auth-page">
      <div className="auth-card auth-card-wide fade-in-up">
        {/* Logo */}
        <div className="auth-logo">
          <span className="logo-icon">⚡</span>
          <span className="logo-text">Daraz<span className="logo-bd">BD</span></span>
        </div>

        <div className="auth-header">
          <h1 className="auth-title">Become a Seller</h1>
          <p className="auth-subtitle">Create your seller account and start listing electronics on cuetEbazar.</p>
        </div>

        {/* Benefits */}
        <div className="auth-benefits">
          {['List unlimited products', 'Reach thousands of buyers', 'BDT & USD pricing', 'Image upload support'].map(b => (
            <div key={b} className="benefit-item">✓ {b}</div>
          ))}
        </div>

        {error && <div className="auth-error">⚠️ {error}</div>}

        <form onSubmit={handleSubmit} className="auth-form" id="seller-register-form">
          <div className="auth-form-row">
            <div className="form-group">
              <label className="form-label" htmlFor="reg-name">Full Name *</label>
              <input
                id="reg-name"
                name="name"
                type="text"
                className="form-input"
                placeholder="Your full name"
                value={form.name}
                onChange={handleChange}
                required
              />
            </div>
            <div className="form-group">
              <label className="form-label" htmlFor="reg-shop">Shop Name</label>
              <input
                id="reg-shop"
                name="shop_name"
                type="text"
                className="form-input"
                placeholder="Your shop/store name"
                value={form.shop_name}
                onChange={handleChange}
              />
            </div>
          </div>

          <div className="form-group">
            <label className="form-label" htmlFor="reg-email">Email Address *</label>
            <input
              id="reg-email"
              name="email"
              type="email"
              className="form-input"
              placeholder="seller@example.com"
              value={form.email}
              onChange={handleChange}
              required
            />
          </div>

          <div className="auth-form-row">
            <div className="form-group">
              <label className="form-label" htmlFor="reg-password">Password *</label>
              <input
                id="reg-password"
                name="password"
                type="password"
                className="form-input"
                placeholder="Min. 6 characters"
                value={form.password}
                onChange={handleChange}
                required
                minLength={6}
              />
            </div>
            <div className="form-group">
              <label className="form-label" htmlFor="reg-confirm">Confirm Password *</label>
              <input
                id="reg-confirm"
                name="confirm_password"
                type="password"
                className="form-input"
                placeholder="Repeat password"
                value={form.confirm_password}
                onChange={handleChange}
                required
              />
            </div>
          </div>

          <button
            type="submit"
            className="btn btn-primary btn-lg w-full"
            disabled={loading}
            id="register-submit-btn"
          >
            {loading
              ? <><span className="spinner" style={{ width: 18, height: 18, borderWidth: 2 }} /> Creating account...</>
              : '🚀 Create Seller Account'}
          </button>
        </form>

        <p className="auth-footer">
          Already have an account?{' '}
          <Link to="/seller/login" className="auth-link">Sign in →</Link>
        </p>

        <Link to="/" className="btn btn-secondary btn-sm w-full" style={{ textAlign: 'center' }}>
          ← Back to Marketplace
        </Link>
      </div>
    </div>
  )
}
