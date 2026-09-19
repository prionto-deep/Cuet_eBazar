import { useEffect, useState } from 'react'
import { useParams, Link, useNavigate } from 'react-router-dom'
import { fetchProduct, formatBDT, formatUSD, deleteProduct, updateProduct } from '../api/client'
import { useAuth } from '../context/AuthContext'
import { useCart } from '../context/CartContext'
import './ProductDetail.css'

const API_BASE = 'http://localhost:8000'

function StarRating({ rating, count }) {
  return (
    <div className="detail-rating">
      <div className="stars">
        {[1,2,3,4,5].map(s => (
          <span key={s} className={s <= Math.round(rating) ? 'star filled' : 'star'}>★</span>
        ))}
      </div>
      <span className="rating-number">{rating?.toFixed(1)}</span>
      <span className="rating-count">({count?.toLocaleString()} reviews)</span>
    </div>
  )
}

export default function ProductDetail() {
  const { id } = useParams()
  const navigate = useNavigate()
  const { seller } = useAuth()
  const { addToCart, cartItems } = useCart()

  const [product, setProduct] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [added, setAdded] = useState(false)

  // Edit modal state
  const [editing, setEditing] = useState(false)
  const [editForm, setEditForm] = useState({})
  const [editImage, setEditImage] = useState(null)       // File object
  const [editImagePreview, setEditImagePreview] = useState(null) // Object URL
  const [editLoading, setEditLoading] = useState(false)
  const [editError, setEditError] = useState(null)

  // Delete state
  const [deleteConfirm, setDeleteConfirm] = useState(false)
  const [deleteLoading, setDeleteLoading] = useState(false)

  useEffect(() => {
    fetchProduct(Number(id))
      .then((p) => {
        setProduct(p)
        setEditForm({
          name: p.name,
          description: p.description || '',
          price_bdt: p.price_bdt,
          brand: p.brand || '',
          stock: p.stock,
          category_id: p.category_id,
        })
        setEditImagePreview(null)
        setEditImage(null)
      })
      .catch(() => setError('Product not found'))
      .finally(() => setLoading(false))
  }, [id])

  const isOwner = seller && product && (seller.id === product.seller_id || seller.is_admin)
  const inCart = cartItems.some((i) => i.id === product?.id)

  const handleAddToCart = () => {
    if (product && product.stock > 0) {
      addToCart(product)
      setAdded(true)
      setTimeout(() => setAdded(false), 2000)
    }
  }

  const handleBuyNow = () => {
    if (product && product.stock > 0) {
      addToCart(product)
      navigate('/cart')
    }
  }

  // Edit handlers
  const handleEditChange = (e) => {
    setEditForm((f) => ({ ...f, [e.target.name]: e.target.value }))
  }

  const handleEditImageChange = (e) => {
    const file = e.target.files[0]
    if (!file) return
    setEditImage(file)
    setEditImagePreview(URL.createObjectURL(file))
  }

  const handleEditSubmit = async (e) => {
    e.preventDefault()
    setEditLoading(true)
    setEditError(null)
    try {
      const fd = new FormData()
      Object.entries(editForm).forEach(([k, v]) => { if (v !== '' && v !== null) fd.append(k, v) })
      if (editImage) fd.append('image', editImage)
      const updated = await updateProduct(product.id, fd)
      setProduct(updated)
      setEditing(false)
      setEditImage(null)
      setEditImagePreview(null)
    } catch (err) {
      setEditError(err.response?.data?.detail || 'Update failed.')
    } finally {
      setEditLoading(false)
    }
  }

  // Delete handler
  const handleDelete = async () => {
    setDeleteLoading(true)
    try {
      await deleteProduct(product.id)
      navigate('/')
    } catch (err) {
      alert(err.response?.data?.detail || 'Delete failed.')
      setDeleteLoading(false)
      setDeleteConfirm(false)
    }
  }

  if (loading) {
    return (
      <div className="page-wrapper container">
        <div className="detail-skeleton">
          <div className="skeleton skeleton-img-lg" />
          <div className="skeleton-info">
            {[200, 300, 150, 80, 250, 200, 100, 50].map((w, i) => (
              <div key={i} className="skeleton" style={{ height: i < 2 ? 20 : i === 3 ? 36 : 14, width: w, marginBottom: 12 }} />
            ))}
          </div>
        </div>
      </div>
    )
  }

  if (error || !product) {
    return (
      <div className="page-wrapper container text-center">
        <div style={{ padding: '5rem 0' }}>
          <div style={{ fontSize: '4rem' }}>😞</div>
          <h2 style={{ marginTop: '1rem', color: 'var(--text-primary)' }}>{error || 'Product not found'}</h2>
          <Link to="/" className="btn btn-primary" style={{ marginTop: '2rem', display: 'inline-flex' }}>
            ← Back to Home
          </Link>
        </div>
      </div>
    )
  }

  const imageUrl = product.image_url?.startsWith('http')
    ? product.image_url
    : `${API_BASE}${product.image_url}`

  return (
    <div className="page-wrapper">
      <div className="container">
        {/* Breadcrumb */}
        <nav className="breadcrumb" aria-label="Breadcrumb">
          <Link to="/" className="breadcrumb-link">Home</Link>
          <span className="breadcrumb-sep">›</span>
          {product.category && (
            <>
              <Link to={`/?category=${product.category.slug}`} className="breadcrumb-link">
                {product.category.icon} {product.category.name}
              </Link>
              <span className="breadcrumb-sep">›</span>
            </>
          )}
          <span className="breadcrumb-current">{product.name}</span>
        </nav>

        <div className="detail-layout">
          {/* Image */}
          <div className="detail-image-section">
            <div className="detail-image-wrap">
              <img
                src={imageUrl}
                alt={product.name}
                className="detail-image"
                onError={(e) => { e.target.src = `https://picsum.photos/seed/fb${product.id}/600/600` }}
              />
            </div>
          </div>

          {/* Info */}
          <div className="detail-info-section">
            {product.brand && (
              <span className="detail-brand">{product.brand}</span>
            )}
            <h1 className="detail-name">{product.name}</h1>

            {product.seller_shop_name && (
              <p className="detail-shop-name">🏪 Sold by <strong>{product.seller_shop_name}</strong></p>
            )}

            <StarRating rating={product.rating} count={product.review_count} />

            {/* Price */}
            <div className="detail-price-box">
              <div className="detail-price-bdt">{formatBDT(product.price_bdt)}</div>
              <div className="detail-price-usd">{formatUSD(product.price_bdt)} USD</div>
              <div className="detail-price-note">
                💱 Exchange rate: 1 USD = ৳110 (approximate)
              </div>
            </div>

            {/* Stock */}
            <div className={`detail-stock ${product.stock > 0 ? 'in-stock' : 'out-of-stock'}`}>
              {product.stock > 0
                ? `✓ In Stock — ${product.stock} units available`
                : '✗ Out of Stock'}
            </div>

            {/* Actions */}
            <div className="detail-actions">
              <button
                className={`btn btn-lg ${added || inCart ? 'btn-success' : 'btn-primary'}`}
                onClick={handleAddToCart}
                disabled={product.stock === 0}
                id="add-to-cart-btn"
                style={{ flex: 1 }}
              >
                {added ? '✓ Added!' : inCart ? '✓ In Cart' : '🛒 Add to Cart'}
              </button>
              <button
                className="btn btn-secondary btn-lg"
                id="buy-now-btn"
                disabled={product.stock === 0}
                style={{ flex: 1 }}
                onClick={handleBuyNow}
              >
                ⚡ Buy Now
              </button>
            </div>

            {/* Seller owner controls */}
            {isOwner && (
              <div className="detail-owner-actions">
                {seller.is_admin && seller.id !== product.seller_id && (
                  <span className="admin-badge">👑 Admin Control</span>
                )}
                <button
                  className="btn btn-outline btn-sm"
                  onClick={() => setEditing(true)}
                  id="edit-product-btn"
                >
                  ✏️ Edit Product
                </button>
                {!deleteConfirm ? (
                  <button
                    className="btn btn-danger btn-sm"
                    onClick={() => setDeleteConfirm(true)}
                    id="delete-product-btn"
                  >
                    🗑 Delete
                  </button>
                ) : (
                  <div className="delete-confirm">
                    <span>Are you sure?</span>
                    <button
                      className="btn btn-danger btn-sm"
                      onClick={handleDelete}
                      disabled={deleteLoading}
                      id="confirm-delete-btn"
                    >
                      {deleteLoading ? 'Deleting...' : 'Yes, Delete'}
                    </button>
                    <button
                      className="btn btn-secondary btn-sm"
                      onClick={() => setDeleteConfirm(false)}
                    >
                      Cancel
                    </button>
                  </div>
                )}
              </div>
            )}

            {/* Description */}
            {product.description && (
              <div className="detail-description">
                <h3 className="detail-section-label">Product Description</h3>
                <p className="detail-description-text">{product.description}</p>
              </div>
            )}

            {/* Meta */}
            <div className="detail-meta-grid">
              {product.category && (
                <div className="meta-item">
                  <span className="meta-label">Category</span>
                  <span className="meta-value">{product.category.icon} {product.category.name}</span>
                </div>
              )}
              {product.brand && (
                <div className="meta-item">
                  <span className="meta-label">Brand</span>
                  <span className="meta-value">{product.brand}</span>
                </div>
              )}
              {product.seller_shop_name && (
                <div className="meta-item">
                  <span className="meta-label">Seller</span>
                  <span className="meta-value">🏪 {product.seller_shop_name}</span>
                </div>
              )}
              <div className="meta-item">
                <span className="meta-label">Stock</span>
                <span className="meta-value">{product.stock} units</span>
              </div>
              <div className="meta-item">
                <span className="meta-label">Rating</span>
                <span className="meta-value">⭐ {product.rating?.toFixed(1)} / 5</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Edit Modal */}
      {editing && (
        <div className="modal-overlay" onClick={() => setEditing(false)}>
          <div className="modal-card fade-in-up" onClick={(e) => e.stopPropagation()}>
            <h2 className="modal-title">✏️ Edit Product</h2>
            {editError && <div className="auth-error">⚠️ {editError}</div>}
            <form onSubmit={handleEditSubmit} className="auth-form">
              {[
                { name: 'name', label: 'Product Name', type: 'text' },
                { name: 'brand', label: 'Brand', type: 'text' },
                { name: 'price_bdt', label: 'Price (BDT)', type: 'number' },
                { name: 'stock', label: 'Stock', type: 'number' },
              ].map(({ name, label, type }) => (
                <div className="form-group" key={name}>
                  <label className="form-label" htmlFor={`edit-${name}`}>{label}</label>
                  <input
                    id={`edit-${name}`}
                    name={name}
                    type={type}
                    className="form-input"
                    value={editForm[name]}
                    onChange={handleEditChange}
                  />
                </div>
              ))}
              <div className="form-group">
                <label className="form-label" htmlFor="edit-description">Description</label>
                <textarea
                  id="edit-description"
                  name="description"
                  className="form-input"
                  rows={3}
                  value={editForm.description}
                  onChange={handleEditChange}
                  style={{ resize: 'vertical' }}
                />
              </div>

              {/* Image upload */}
              <div className="form-group">
                <label className="form-label" htmlFor="edit-image">Product Photo</label>
                <div className="edit-image-preview-wrap">
                  <img
                    src={editImagePreview || (product.image_url?.startsWith('http') ? product.image_url : `${API_BASE}${product.image_url}`)}
                    alt="Current product"
                    className="edit-image-preview"
                    onError={(e) => { e.target.src = `https://picsum.photos/seed/fb${product.id}/120/120` }}
                  />
                  {editImagePreview && (
                    <span className="edit-image-new-badge">New image selected</span>
                  )}
                </div>
                <input
                  id="edit-image"
                  name="image"
                  type="file"
                  accept="image/jpeg,image/png,image/webp,image/gif"
                  className="form-input"
                  onChange={handleEditImageChange}
                  style={{ paddingTop: '0.5rem' }}
                />
                <p style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '0.3rem' }}>
                  Leave empty to keep the current photo.
                </p>
              </div>
              <div className="modal-actions">
                <button type="submit" className="btn btn-primary" disabled={editLoading} id="save-edit-btn">
                  {editLoading ? 'Saving...' : '💾 Save Changes'}
                </button>
                <button type="button" className="btn btn-secondary" onClick={() => setEditing(false)}>
                  Cancel
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  )
}
