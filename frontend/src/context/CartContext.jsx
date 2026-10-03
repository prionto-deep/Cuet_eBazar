import { createContext, useContext, useState, useEffect } from 'react'
import { useAuth } from './AuthContext'

const CartContext = createContext(null)

const CART_KEY = 'cart_items'

export function CartProvider({ children }) {
  const { buyer } = useAuth()
  const [cartItems, setCartItems] = useState(() => {
    try {
      const stored = localStorage.getItem(CART_KEY)
      const parsed = stored ? JSON.parse(stored) : []
      return Array.isArray(parsed) ? parsed : []
    } catch {
      return []
    }
  })

  // Persist cart to localStorage whenever it changes
  useEffect(() => {
    localStorage.setItem(CART_KEY, JSON.stringify(cartItems))
  }, [cartItems])

  // Clear cart when buyer logs out
  useEffect(() => {
    if (!buyer) {
      setCartItems([])
      localStorage.removeItem(CART_KEY)
    }
  }, [buyer])

  const addToCart = (product, quantity = 1) => {
    setCartItems((prev) => {
      const existing = prev.find((i) => i.id === product.id)
      if (existing) {
        return prev.map((i) =>
          i.id === product.id
            ? { ...i, qty: Math.min(i.qty + quantity, product.stock) }
            : i
        )
      }
      return [...prev, { ...product, qty: quantity }]
    })
  }

  const removeFromCart = (productId) => {
    setCartItems((prev) => prev.filter((i) => i.id !== productId))
  }

  const updateQty = (productId, qty) => {
    if (qty <= 0) {
      removeFromCart(productId)
      return
    }
    setCartItems((prev) =>
      prev.map((i) => (i.id === productId ? { ...i, qty } : i))
    )
  }

  const clearCart = () => {
    setCartItems([])
    localStorage.removeItem(CART_KEY)
  }

  const totalItems = cartItems.reduce((sum, i) => sum + i.qty, 0)
  const totalPrice = cartItems.reduce((sum, i) => sum + i.price_bdt * i.qty, 0)

  return (
    <CartContext.Provider value={{ cartItems, addToCart, removeFromCart, updateQty, clearCart, totalItems, totalPrice }}>
      {children}
    </CartContext.Provider>
  )
}

export const useCart = () => {
  const ctx = useContext(CartContext)
  if (!ctx) throw new Error('useCart must be used within CartProvider')
  return ctx
}
