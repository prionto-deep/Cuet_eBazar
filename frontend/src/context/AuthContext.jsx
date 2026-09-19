import { createContext, useContext, useState, useEffect } from 'react'
import { fetchMe, fetchBuyerMe } from '../api/client'

const AuthContext = createContext(null)

export function AuthProvider({ children }) {
  const [seller, setSeller] = useState(null)
  const [buyer, setBuyer] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const sellerToken = localStorage.getItem('token')
    const buyerToken = localStorage.getItem('buyer_token')

    const promises = []

    if (sellerToken) {
      promises.push(
        fetchMe()
          .then(setSeller)
          .catch(() => {
            localStorage.removeItem('token')
            localStorage.removeItem('seller')
          })
      )
    }

    if (buyerToken) {
      promises.push(
        fetchBuyerMe()
          .then(setBuyer)
          .catch(() => {
            localStorage.removeItem('buyer_token')
            localStorage.removeItem('buyer')
          })
      )
    }

    Promise.allSettled(promises).finally(() => setLoading(false))
  }, [])

  // Seller auth
  const login = (token, sellerData) => {
    localStorage.setItem('token', token)
    localStorage.setItem('seller', JSON.stringify(sellerData))
    setSeller(sellerData)
  }

  const logout = () => {
    localStorage.removeItem('token')
    localStorage.removeItem('seller')
    setSeller(null)
  }

  // Buyer auth
  const loginBuyer = (token, buyerData) => {
    localStorage.setItem('buyer_token', token)
    localStorage.setItem('buyer', JSON.stringify(buyerData))
    setBuyer(buyerData)
  }

  const logoutBuyer = () => {
    localStorage.removeItem('buyer_token')
    localStorage.removeItem('buyer')
    setBuyer(null)
  }

  return (
    <AuthContext.Provider value={{ seller, buyer, loading, login, logout, loginBuyer, logoutBuyer }}>
      {children}
    </AuthContext.Provider>
  )
}

export const useAuth = () => {
  const ctx = useContext(AuthContext)
  if (!ctx) throw new Error('useAuth must be used within AuthProvider')
  return ctx
}
