import axios from 'axios'

const API_BASE = 'http://localhost:8000'

export const USD_RATE = 110 // 1 USD = 110 BDT

export const formatBDT = (amount) =>
  `৳${Number(amount).toLocaleString('en-IN')}`

export const formatUSD = (amountBDT) =>
  `$${(amountBDT / USD_RATE).toFixed(2)}`

const api = axios.create({
  baseURL: API_BASE,
  timeout: 15000,
})

// Attach JWT token to every request if present
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

// ── Categories ──────────────────────────────────────────────────────────────
export const fetchCategories = () =>
  api.get('/categories').then((r) => r.data)

// ── Products ─────────────────────────────────────────────────────────────────
export const fetchProducts = (params = {}) =>
  api.get('/products', { params }).then((r) => r.data)

export const fetchProduct = (id) =>
  api.get(`/products/${id}`).then((r) => r.data)

export const createProduct = (formData) =>
  api.post('/products', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  }).then((r) => r.data)

// ── Auth ─────────────────────────────────────────────────────────────────────
export const loginSeller = (credentials) =>
  api.post('/auth/login', credentials).then((r) => r.data)

export const registerSeller = (data) =>
  api.post('/auth/register', data).then((r) => r.data)

export const fetchMe = () =>
  api.get('/auth/me').then((r) => r.data)

export default api
