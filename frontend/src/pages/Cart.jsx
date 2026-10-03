import { useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useCart } from '../context/CartContext'
import { useAuth } from '../context/AuthContext'
import { placeOrder, formatBDT } from '../api/client'
import './Cart.css'

import { API_BASE } from '../api/config'

export default function Cart() {
  const { cartItems, removeFromCart, updateQty, clearCart, totalItems, totalPrice } = useCart()
  const { buyer } = useAuth()
  const navigate = useNavigate()

  const [ordering, setOrdering] = useState(false)
  const [orderResult, setOrderResult] = useState(null)
  const [orderError, setOrderError] = useState(null)

  const handleCheckout = async () => {
    if (!buyer) {
      navigate('/buyer/login', { state: { from: '/cart' } })
      return
    }
    setOrdering(true)
    setOrderError(null)
    try {
      const items = cartItems.map((i) => ({ product_id: i.id, quantity: i.qty }))
      const result = await placeOrder(items)
      setOrderResult(result)
      clearCart()
    } catch (err) {
      setOrderError(err.response?.data?.detail || 'Order failed. Please try again.')
    } finally {
      setOrdering(false)
    }
  }

  if (orderResult) {
    return (
      <div className="cart-page">
        <div className="cart-container">
          <div className="order-success fade-in-up">
            <div className="order-success-icon">🎉</div>
            <h1 className="order-success-title">Order Placed!</h1>
            <p className="order-success-id">Order #{orderResult.order_id}</p>
            <p className="order-success-msg">{orderResult.message}</p>

            <div className="order-items-list">
              {orderResult.items.map((item) => (
                <div key={item.product_id} className="order-item-row">
                  <span className="order-item-name">{item.product_name}</span>
                  <span className="order-item-qty">× {item.quantity}</span>
                  <span className="order-item-subtotal">{formatBDT(item.subtotal)}</span>
                </div>
              ))}
            </div>

            <div className="order-total-row">
              <span>Total Paid</span>
              <span className="order-total-amount">{formatBDT(orderResult.total)}</span>
            </div>

            <div className="order-actions">
              <Link to="/" className="btn btn-primary">🏠 Continue Shopping</Link>
            </div>
          </div>
        </div>
      </div>
    )
  }

  if (cartItems.length === 0) {
    return (
      <div className="cart-page">
        <div className="cart-container">
          <div className="cart-empty fade-in-up">
            <div className="cart-empty-icon">🛒</div>
            <h2 className="cart-empty-title">Your cart is empty</h2>
            <p className="cart-empty-sub">Add some products to get started!</p>
            <Link to="/" className="btn btn-primary">Browse Products</Link>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="cart-page">
      <div className="cart-container">
        <h1 className="cart-title">🛒 Your Cart <span className="cart-count-badge">{totalItems}</span></h1>

        <div className="cart-layout">
          {/* Items */}
          <div className="cart-items">
            {cartItems.map((item) => {
              const imageUrl = item.image_url?.startsWith('http')
                ? item.image_url
                : `${API_BASE}${item.image_url}`

              return (
                <div key={item.id} className="cart-item fade-in-up">
                  <img
                    src={imageUrl}
                    alt={item.name}
                    className="cart-item-image"
                    onError={(e) => { e.target.src = `https://picsum.photos/seed/fb${item.id}/80/80` }}
                  />
                  <div className="cart-item-info">
                    <h3 className="cart-item-name">{item.name}</h3>
                    {item.seller_shop_name && (
                      <p className="cart-item-shop">🏪 {item.seller_shop_name}</p>
                    )}
                    <p className="cart-item-price">{formatBDT(item.price_bdt)}</p>
                  </div>
                  <div className="cart-item-controls">
                    <div className="qty-stepper">
                      <button
                        className="qty-btn"
                        onClick={() => updateQty(item.id, item.qty - 1)}
                        id={`qty-dec-${item.id}`}
                      >−</button>
                      <span className="qty-value">{item.qty}</span>
                      <button
                        className="qty-btn"
                        onClick={() => updateQty(item.id, item.qty + 1)}
                        disabled={item.qty >= item.stock}
                        id={`qty-inc-${item.id}`}
                      >+</button>
                    </div>
                    <p className="cart-item-subtotal">{formatBDT(item.price_bdt * item.qty)}</p>
                    <button
                      className="cart-remove-btn"
                      onClick={() => removeFromCart(item.id)}
                      id={`remove-${item.id}`}
                    >🗑 Remove</button>
                  </div>
                </div>
              )
            })}
          </div>

          {/* Summary */}
          <div className="cart-summary">
            <h2 className="summary-title">Order Summary</h2>
            <div className="summary-row">
              <span>Items ({totalItems})</span>
              <span>{formatBDT(totalPrice)}</span>
            </div>
            <div className="summary-row summary-total">
              <span>Total</span>
              <span>{formatBDT(totalPrice)}</span>
            </div>

            {orderError && <div className="auth-error" style={{ marginBottom: '1rem' }}>⚠️ {orderError}</div>}

            {!buyer && (
              <p className="summary-login-hint">
                <Link to="/buyer/login" state={{ from: '/cart' }} className="auth-link">
                  Sign in as buyer
                </Link>{' '}to checkout
              </p>
            )}

            <button
              className="btn btn-primary btn-lg w-full"
              onClick={handleCheckout}
              disabled={ordering}
              id="checkout-btn"
            >
              {ordering
                ? <><span className="spinner" style={{ width: 18, height: 18, borderWidth: 2 }} /> Processing...</>
                : buyer ? '⚡ Place Order' : '🔐 Login to Checkout'}
            </button>

            <button
              className="btn btn-secondary btn-sm w-full"
              onClick={clearCart}
              style={{ marginTop: '0.75rem' }}
              id="clear-cart-btn"
            >
              Clear Cart
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}
