import { Link } from 'react-router-dom'
import { formatBDT, formatUSD } from '../api/client'
import { useCart } from '../context/CartContext'
import './ProductCard.css'

const API_BASE = 'http://localhost:8000'

function StarRating({ rating }) {
  return (
    <div className="stars" aria-label={`Rating: ${rating} out of 5`}>
      {[1, 2, 3, 4, 5].map((star) => (
        <span key={star} className={star <= Math.round(rating) ? 'star filled' : 'star'}>
          ★
        </span>
      ))}
    </div>
  )
}

export default function ProductCard({ product }) {
  const { addToCart, cartItems } = useCart()

  const imageUrl = product.image_url?.startsWith('http')
    ? product.image_url
    : `${API_BASE}${product.image_url}`

  const isInStock = product.stock > 0
  const inCart = cartItems.some((i) => i.id === product.id)

  const handleAddToCart = (e) => {
    e.preventDefault()
    e.stopPropagation()
    if (isInStock) addToCart(product)
  }

  return (
    <Link
      to={`/products/${product.id}`}
      className="product-card fade-in-up"
      id={`product-card-${product.id}`}
    >
      {/* Image */}
      <div className="product-card-image-wrap">
        <img
          src={imageUrl}
          alt={product.name}
          className="product-card-image"
          loading="lazy"
          onError={(e) => {
            e.target.src = `https://picsum.photos/seed/fallback${product.id}/400/400`
          }}
        />
        {!isInStock && (
          <div className="out-of-stock-overlay">Out of Stock</div>
        )}
        {product.category && (
          <span className="product-category-badge">
            {product.category.icon} {product.category.name}
          </span>
        )}
      </div>

      {/* Info */}
      <div className="product-card-info">
        {product.brand && (
          <span className="product-brand">{product.brand}</span>
        )}
        <h3 className="product-name">{product.name}</h3>

        {product.seller_shop_name && (
          <p className="product-shop-name">🏪 {product.seller_shop_name}</p>
        )}

        <div className="product-rating-row">
          <StarRating rating={product.rating} />
          <span className="review-count">({product.review_count?.toLocaleString()})</span>
        </div>

        <div className="product-price-section">
          <span className="price-bdt">{formatBDT(product.price_bdt)}</span>
          <span className="price-usd">{formatUSD(product.price_bdt)}</span>
        </div>

        {isInStock ? (
          <div className="stock-info in-stock">✓ In Stock ({product.stock})</div>
        ) : (
          <div className="stock-info out-of-stock">✗ Out of Stock</div>
        )}

        <button
          className={`btn w-full add-to-cart-btn ${inCart ? 'btn-success' : 'btn-primary'}`}
          onClick={handleAddToCart}
          disabled={!isInStock}
          id={`add-to-cart-${product.id}`}
        >
          {inCart ? '✓ In Cart' : '🛒 Add to Cart'}
        </button>
      </div>
    </Link>
  )
}
