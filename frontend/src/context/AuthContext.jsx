import { createContext, useContext, useState, useEffect } from 'react'
import { fetchMe } from '../api/client'

const AuthContext = createContext(null)

export function AuthProvider({ children }) {
  const [seller, setSeller] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const token = localStorage.getItem('token')
    if (token) {
      fetchMe()
        .then(setSeller)
        .catch(() => {
          localStorage.removeItem('token')
          localStorage.removeItem('seller')
        })
        .finally(() => setLoading(false))
    } else {
      setLoading(false)
    }
  }, [])

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

  return (
    <AuthContext.Provider value={{ seller, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  )
}

export const useAuth = () => {
  const ctx = useContext(AuthContext)
  if (!ctx) throw new Error('useAuth must be used within AuthProvider')
  return ctx
}
