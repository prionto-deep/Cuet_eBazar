import axios from 'axios'

import { API_BASE } from './config'

export const USD_RATE = 110 // 1 USD = 110 BDT

export const formatBDT = (amount) =>
  `৳${Number(amount).toLocaleString('en-IN')}`

export const formatUSD = (amountBDT) =>
  `$${(amountBDT / USD_RATE).toFixed(2)}`

const api = axios.create({
  baseURL: API_BASE,
  timeout: 15000,
})

// Attach JWT token — seller token takes priority unless route is buyer-specific
api.interceptors.request.use((config) => {
  const url = config.url || ''
  const isBuyerRoute = url.startsWith('/auth/buyer') || url.startsWith('/orders')
  const token = isBuyerRoute
    ? localStorage.getItem('buyer_token')
    : (localStorage.getItem('token') || localStorage.getItem('buyer_token'))
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

export const updateProduct = (id, formData) =>
  api.put(`/products/${id}`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  }).then((r) => r.data)

export const deleteProduct = (id) =>
  api.delete(`/products/${id}`)

// ── Seller Auth ───────────────────────────────────────────────────────────────
export const loginSeller = (credentials) =>
  api.post('/auth/login', credentials).then((r) => r.data)

export const registerSeller = (data) =>
  api.post('/auth/register', data).then((r) => r.data)

export const fetchMe = () =>
  api.get('/auth/me').then((r) => r.data)

// ── Buyer Auth ────────────────────────────────────────────────────────────────
export const loginBuyer = (credentials) =>
  api.post('/auth/buyer/login', credentials).then((r) => r.data)

export const registerBuyer = (data) =>
  api.post('/auth/buyer/register', data).then((r) => r.data)

export const fetchBuyerMe = () =>
  api.get('/auth/buyer/me').then((r) => r.data)

// ── Orders ────────────────────────────────────────────────────────────────────
export const placeOrder = (items) =>
  api.post('/orders', { items }).then((r) => r.data)

// ── Admin ─────────────────────────────────────────────────────────────────────
export const adminFetchProducts = (params = {}) =>
  api.get('/admin/products', { params }).then((r) => r.data)

export const adminDeleteProduct = (id) =>
  api.delete(`/admin/products/${id}`)

export const adminUpdateProductImage = (id, formData) =>
  api.patch(`/admin/products/${id}/image`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  }).then((r) => r.data)

export default api
