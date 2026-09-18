import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import { fetchProduct, formatBDT, formatUSD } from '../api/client'
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
  const [product, setProduct] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [added, setAdded] = useState(false)

  useEffect(() => {
    fetchProduct(Number(id))
      .then(setProduct)
      .catch(() => setError('Product not found'))
      .finally(() => setLoading(false))
  }, [id])

  const handleAddToCart = () => {
    setAdded(true)
    setTimeout(() => setAdded(false), 2000)
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
                className={`btn btn-primary btn-lg ${added ? 'btn-success' : ''}`}
                onClick={handleAddToCart}
                disabled={product.stock === 0}
                id="add-to-cart-btn"
                style={{ flex: 1 }}
              >
                {added ? '✓ Added to Cart!' : '🛒 Add to Cart'}
              </button>
              <button
                className="btn btn-secondary btn-lg"
                id="buy-now-btn"
                disabled={product.stock === 0}
                style={{ flex: 1 }}
              >
                ⚡ Buy Now
              </button>
            </div>

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
    </div>
  )
}
