// Base URL of the backend API (FastAPI).
// Set VITE_API_BASE_URL at build time (e.g. in Netlify's environment variables)
// to point the deployed frontend at the hosted backend, e.g.
//   VITE_API_BASE_URL=https://your-backend.example.com
// In local development it falls back to the local backend; in production
// builds without the variable it falls back to relative paths ('').
const rawBase =
  import.meta.env.VITE_API_BASE_URL ??
  (import.meta.env.DEV ? 'http://localhost:8000' : '')

export const API_BASE = rawBase.replace(/\/+$/, '')
