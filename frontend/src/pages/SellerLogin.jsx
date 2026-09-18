import { useState } from 'react'
import { Link, useNavigate, useLocation } from 'react-router-dom'
import { loginSeller } from '../api/client'
import { useAuth } from '../context/AuthContext'
import './AuthPages.css'

export default function SellerLogin() {
  const { login } = useAuth()
  const navigate = useNavigate()
  const location = useLocation()
  const redirectTo = location.state?.from || '/upload'

  const [form, setForm] = useState({ email: '', password: '' })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleChange = (e) => {
    setForm((f) => ({ ...f, [e.target.name]: e.target.value }))
    setError(null)
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    setError(null)
    try {
      const data = await loginSeller(form)
      login(data.access_token, data.seller)
      navigate(redirectTo)
    } catch (err) {
      setError(err.response?.data?.detail || 'Login failed. Check your credentials.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="auth-page">
      <div className="auth-card fade-in-up">
        {/* Logo */}
        <div className="auth-logo">
          <span className="logo-icon">⚡</span>
          <span className="logo-text">Daraz<span className="logo-bd">BD</span></span>
        </div>

        <div className="auth-header">
          <h1 className="auth-title">Seller Login</h1>
          <p className="auth-subtitle">Sign in to your seller account to manage and list products.</p>
        </div>

        {error && <div className="auth-error">⚠️ {error}</div>}

        <form onSubmit={handleSubmit} className="auth-form" id="seller-login-form">
          <div className="form-group">
            <label className="form-label" htmlFor="login-email">Email Address</label>
            <input
              id="login-email"
              name="email"
              type="email"
              className="form-input"
              placeholder="seller@example.com"
              value={form.email}
              onChange={handleChange}
              required
              autoComplete="email"
            />
          </div>
          <div className="form-group">
            <label className="form-label" htmlFor="login-password">Password</label>
            <input
              id="login-password"
              name="password"
              type="password"
              className="form-input"
              placeholder="••••••••"
              value={form.password}
              onChange={handleChange}
              required
              autoComplete="current-password"
            />
          </div>

          <button
            type="submit"
            className="btn btn-primary btn-lg w-full"
            disabled={loading}
            id="login-submit-btn"
          >
            {loading
              ? <><span className="spinner" style={{ width: 18, height: 18, borderWidth: 2 }} /> Signing in...</>
              : '🔐 Sign In'}
          </button>
        </form>

        <p className="auth-footer">
          Don't have a seller account?{' '}
          <Link to="/seller/register" className="auth-link">Register here →</Link>
        </p>

        <Link to="/" className="btn btn-secondary btn-sm w-full" style={{ textAlign: 'center' }}>
          ← Back to Marketplace
        </Link>
      </div>
    </div>
  )
}
