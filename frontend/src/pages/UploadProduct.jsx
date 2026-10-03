import { useState, useEffect } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import { createProduct, fetchCategories } from '../api/client'
import './UploadProduct.css'

import { API_BASE } from '../api/config'

export default function UploadProduct() {
  const navigate = useNavigate()
  const [categories, setCategories] = useState([])
  const [loading, setLoading] = useState(false)
  const [success, setSuccess] = useState(null)
  const [error, setError] = useState(null)
  const [imagePreview, setImagePreview] = useState(null)
  const [form, setForm] = useState({
    name: '',
    description: '',
    price_bdt: '',
    brand: '',
    stock: '',
    category_id: '',
    image: null,
  })

  useEffect(() => {
    fetchCategories().then(setCategories).catch(console.error)
  }, [])

  const usdPreview = form.price_bdt
    ? `≈ $${(Number(form.price_bdt) / 110).toFixed(2)} USD`
    : ''

  const handleChange = (e) => {
    const { name, value } = e.target
    setForm((f) => ({ ...f, [name]: value }))
    setError(null)
  }

  const handleImageChange = (e) => {
    const file = e.target.files[0]
    if (!file) return
    if (file.size > 10 * 1024 * 1024) {
      setError('Image must be under 10MB')
      return
    }
    setForm((f) => ({ ...f, image: file }))
    const reader = new FileReader()
    reader.onload = () => setImagePreview(reader.result)
    reader.readAsDataURL(file)
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError(null)

    if (!form.name.trim()) return setError('Product name is required')
    if (!form.price_bdt || Number(form.price_bdt) <= 0) return setError('Price must be a positive number')
    if (!form.category_id) return setError('Please select a category')

    const fd = new FormData()
    fd.append('name', form.name.trim())
    fd.append('description', form.description.trim())
    fd.append('price_bdt', form.price_bdt)
    fd.append('brand', form.brand.trim())
    fd.append('stock', form.stock || '0')
    fd.append('category_id', form.category_id)
    if (form.image) fd.append('image', form.image)

    setLoading(true)
    try {
      const product = await createProduct(fd)
      setSuccess(product)
      setForm({ name:'', description:'', price_bdt:'', brand:'', stock:'', category_id:'', image:null })
      setImagePreview(null)
    } catch (err) {
      setError(err.response?.data?.detail || 'Upload failed. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  if (success) {
    const img = success.image_url?.startsWith('http')
      ? success.image_url
      : `${API_BASE}${success.image_url}`
    return (
      <div className="page-wrapper container">
        <div className="upload-success-card fade-in-up">
          <div className="success-icon">🎉</div>
          <h2 className="success-title">Product Listed Successfully!</h2>
          <div className="success-product-preview">
            {success.image_url && (
              <img src={img} alt={success.name} className="success-product-img"
                onError={(e) => { e.target.style.display='none' }} />
            )}
            <div>
              <p className="success-product-name">{success.name}</p>
              <p className="success-product-price">৳{Number(success.price_bdt).toLocaleString()}</p>
            </div>
          </div>
          <div className="success-actions">
            <button className="btn btn-primary" onClick={() => setSuccess(null)}>
              + List Another Product
            </button>
            <Link to={`/products/${success.id}`} className="btn btn-secondary">
              View Product
            </Link>
            <Link to="/" className="btn btn-outline">
              Back to Home
            </Link>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="page-wrapper">
      <div className="container upload-container">
        {/* Header */}
        <div className="upload-header">
          <h1 className="upload-title">📤 List a Product</h1>
          <p className="upload-subtitle">
            Add a new electronics product to the marketplace. Prices in BDT — USD shown automatically.
          </p>
        </div>

        <div className="upload-layout">
          {/* Form */}
          <form className="upload-form" onSubmit={handleSubmit} id="upload-product-form">
            {/* Error */}
            {error && (
              <div className="form-error-banner">
                ⚠️ {error}
              </div>
            )}

            {/* Name + Brand row */}
            <div className="form-row">
              <div className="form-group">
                <label className="form-label" htmlFor="product-name">Product Name *</label>
                <input
                  id="product-name"
                  name="name"
                  type="text"
                  className="form-input"
                  placeholder="e.g. Samsung Galaxy S25 Ultra"
                  value={form.name}
                  onChange={handleChange}
                  required
                />
              </div>
              <div className="form-group">
                <label className="form-label" htmlFor="product-brand">Brand</label>
                <input
                  id="product-brand"
                  name="brand"
                  type="text"
                  className="form-input"
                  placeholder="e.g. Samsung, Apple, Sony..."
                  value={form.brand}
                  onChange={handleChange}
                />
              </div>
            </div>

            {/* Category */}
            <div className="form-group">
              <label className="form-label" htmlFor="product-category">Category *</label>
              <select
                id="product-category"
                name="category_id"
                className="form-input form-select"
                value={form.category_id}
                onChange={handleChange}
                required
              >
                <option value="">— Select a category —</option>
                {categories.map((cat) => (
                  <option key={cat.id} value={cat.id}>
                    {cat.icon} {cat.name}
                  </option>
                ))}
              </select>
            </div>

            {/* Price + Stock row */}
            <div className="form-row">
              <div className="form-group">
                <label className="form-label" htmlFor="product-price">Price (BDT) *</label>
                <div className="price-input-wrap">
                  <span className="price-symbol">৳</span>
                  <input
                    id="product-price"
                    name="price_bdt"
                    type="number"
                    className="form-input price-input"
                    placeholder="0"
                    value={form.price_bdt}
                    onChange={handleChange}
                    min={1}
                    step={1}
                    required
                  />
                </div>
                {usdPreview && (
                  <span className="usd-hint">{usdPreview}</span>
                )}
              </div>
              <div className="form-group">
                <label className="form-label" htmlFor="product-stock">Stock Quantity</label>
                <input
                  id="product-stock"
                  name="stock"
                  type="number"
                  className="form-input"
                  placeholder="0"
                  value={form.stock}
                  onChange={handleChange}
                  min={0}
                />
              </div>
            </div>

            {/* Description */}
            <div className="form-group">
              <label className="form-label" htmlFor="product-description">Description</label>
              <textarea
                id="product-description"
                name="description"
                className="form-input form-textarea"
                placeholder="Describe the product specs, features, and condition..."
                value={form.description}
                onChange={handleChange}
                rows={4}
              />
            </div>

            {/* Submit */}
            <button
              type="submit"
              className="btn btn-primary btn-lg w-full"
              disabled={loading}
              id="submit-product-btn"
            >
              {loading ? (
                <><span className="spinner" style={{ width: 20, height: 20, borderWidth: 2 }} /> Uploading...</>
              ) : (
                '📤 List Product on Marketplace'
              )}
            </button>
          </form>

          {/* Image upload panel */}
          <div className="upload-image-panel">
            <div className="form-label" style={{ marginBottom: 8 }}>Product Image</div>
            <label className="image-drop-zone" htmlFor="product-image-input">
              {imagePreview ? (
                <img src={imagePreview} alt="Preview" className="image-preview" />
              ) : (
                <div className="drop-zone-placeholder">
                  <span className="drop-icon">📸</span>
                  <p className="drop-text">Click to upload image</p>
                  <p className="drop-hint">JPG, PNG, WEBP — max 10MB</p>
                </div>
              )}
            </label>
            <input
              id="product-image-input"
              type="file"
              accept="image/*"
              style={{ display: 'none' }}
              onChange={handleImageChange}
            />
            {imagePreview && (
              <button
                type="button"
                className="btn btn-danger btn-sm w-full"
                style={{ marginTop: 8 }}
                onClick={() => { setImagePreview(null); setForm(f => ({ ...f, image: null })) }}
              >
                Remove Image
              </button>
            )}

            {/* Tips */}
            <div className="upload-tips">
              <h4 className="tips-title">💡 Listing Tips</h4>
              <ul className="tips-list">
                <li>Use a clear, high-quality image</li>
                <li>Include key specs in description</li>
                <li>Set accurate stock count</li>
                <li>Price in BDT — USD auto-converts</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
