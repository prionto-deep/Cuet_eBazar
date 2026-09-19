import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { registerBuyer } from '../api/client'
import { useAuth } from '../context/AuthContext'
import './AuthPages.css'

export default function BuyerRegister() {
  const { loginBuyer } = useAuth()
  const navigate = useNavigate()

  const [form, setForm] = useState({ name: '', email: '', password: '', confirm_password: '' })
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleChange = (e) => {
    setForm((f) => ({ ...f, [e.target.name]: e.target.value }))
    setError(null)
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (form.password !== form.confirm_password) {
      setError('Passwords do not match.')
      return
    }
    if (form.password.length < 6) {
      setError('Password must be at least 6 characters.')
      return
    }
    setLoading(true)
    setError(null)
    try {
      const data = await registerBuyer({ name: form.name, email: form.email, password: form.password })
      loginBuyer(data.access_token, data.buyer)
      navigate('/')
    } catch (err) {
      setError(err.response?.data?.detail || 'Registration failed. Please try again.')
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
          <span className="logo-text">cuet<span className="logo-bd">Ebazar</span></span>
        </div>

        <div className="auth-header">
          <h1 className="auth-title">Create Buyer Account</h1>
          <p className="auth-subtitle">Join cuetEbazar and start shopping for the best electronics.</p>
        </div>

        {error && <div className="auth-error">⚠️ {error}</div>}

        <form onSubmit={handleSubmit} className="auth-form" id="buyer-register-form">
          <div className="form-group">
            <label className="form-label" htmlFor="buyer-reg-name">Full Name *</label>
            <input
              id="buyer-reg-name"
              name="name"
              type="text"
              className="form-input"
              placeholder="Your full name"
              value={form.name}
              onChange={handleChange}
              required
              autoComplete="name"
            />
          </div>

          <div className="form-group">
            <label className="form-label" htmlFor="buyer-reg-email">Email Address *</label>
            <input
              id="buyer-reg-email"
              name="email"
              type="email"
              className="form-input"
              placeholder="buyer@example.com"
              value={form.email}
              onChange={handleChange}
              required
              autoComplete="email"
            />
          </div>

          <div className="auth-form-row">
            <div className="form-group">
              <label className="form-label" htmlFor="buyer-reg-password">Password *</label>
              <input
                id="buyer-reg-password"
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
              <label className="form-label" htmlFor="buyer-reg-confirm">Confirm Password *</label>
              <input
                id="buyer-reg-confirm"
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
            id="buyer-register-submit-btn"
          >
            {loading
              ? <><span className="spinner" style={{ width: 18, height: 18, borderWidth: 2 }} /> Creating account...</>
              : '🛍️ Create Account'}
          </button>
        </form>

        <p className="auth-footer">
          Already have a buyer account?{' '}
          <Link to="/buyer/login" className="auth-link">Sign in →</Link>
        </p>
        <p className="auth-footer">
          Want to sell?{' '}
          <Link to="/seller/register" className="auth-link">Register as a seller →</Link>
        </p>

        <Link to="/" className="btn btn-secondary btn-sm w-full" style={{ textAlign: 'center' }}>
          ← Back to Marketplace
        </Link>
      </div>
    </div>
  )
}
