import { useState, useEffect, useCallback, useRef } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import {
  adminFetchProducts,
  adminDeleteProduct,
  adminUpdateProductImage,
  fetchCategories,
  formatBDT,
} from '../api/client'
import './AdminDashboard.css'

const API_BASE = 'http://localhost:8000'

function ConfirmModal({ product, onConfirm, onCancel }) {
  return (
    <div className="modal-overlay" onClick={onCancel}>
      <div className="modal-box" onClick={(e) => e.stopPropagation()}>
        <div className="modal-icon">🗑️</div>
        <h3 className="modal-title">Delete Product?</h3>
        <p className="modal-desc">
          You are about to permanently delete <strong>"{product?.name}"</strong>.
          This action cannot be undone and will also remove the product photo from storage.
        </p>
        <div className="modal-actions">
          <button className="btn btn-danger" onClick={onConfirm} id="confirm-delete-btn">
            Yes, Delete Permanently
          </button>
          <button className="btn btn-secondary" onClick={onCancel} id="cancel-delete-btn">
            Cancel
          </button>
        </div>
      </div>
    </div>
  )
}

function ImageEditModal({ product, onSave, onCancel }) {
  const [mode, setMode] = useState('url') // 'url' | 'file'
  const [url, setUrl] = useState(product?.image_url || '')
  const [file, setFile] = useState(null)
  const [preview, setPreview] = useState(null)
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState('')

  const handleFile = (e) => {
    const f = e.target.files[0]
    if (!f) return
    setFile(f)
    const reader = new FileReader()
    reader.onload = () => setPreview(reader.result)
    reader.readAsDataURL(f)
  }

  const handleSave = async () => {
    setSaving(true)
    setError('')
    try {
      const fd = new FormData()
      if (mode === 'file' && file) {
        fd.append('image', file)
      } else if (mode === 'url') {
        fd.append('image_url', url.trim())
      }
      const updated = await adminUpdateProductImage(product.id, fd)
      onSave(updated)
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to update image.')
    } finally {
      setSaving(false)
    }
  }

  const currentImg = product?.image_url?.startsWith('http')
    ? product.image_url
    : `${API_BASE}${product?.image_url}`

  return (
    <div className="modal-overlay" onClick={onCancel}>
      <div className="modal-box modal-wide" onClick={(e) => e.stopPropagation()}>
        <div className="modal-icon">🖼️</div>
        <h3 className="modal-title">Edit Product Photo</h3>
        <p className="modal-desc-sm">Product: <strong>{product?.name}</strong></p>

        <div className="img-edit-current">
          <img src={currentImg} alt="Current" className="img-edit-thumb"
            onError={(e) => { e.target.src = 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=200&q=60' }} />
          <span className="img-edit-label">Current photo</span>
        </div>

        <div className="img-edit-tabs">
          <button
            className={`img-tab ${mode === 'url' ? 'active' : ''}`}
            onClick={() => setMode('url')}
          >🔗 Use URL</button>
          <button
            className={`img-tab ${mode === 'file' ? 'active' : ''}`}
            onClick={() => setMode('file')}
          >📁 Upload File</button>
        </div>

        {mode === 'url' && (
          <div className="img-edit-url-wrap">
            <input
              className="form-input"
              type="url"
              placeholder="https://example.com/product.jpg"
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              id="image-url-input"
            />
            {url && (
              <img src={url} alt="Preview" className="img-edit-preview"
                onError={(e) => { e.target.style.display = 'none' }} />
            )}
          </div>
        )}

        {mode === 'file' && (
          <div className="img-edit-file-wrap">
            <label className="img-upload-label" htmlFor="admin-img-file">
              {preview
                ? <img src={preview} alt="New" className="img-edit-preview" />
                : <><span style={{ fontSize: '2rem' }}>📸</span><span>Click to choose image</span></>
              }
            </label>
            <input id="admin-img-file" type="file" accept="image/*" style={{ display: 'none' }} onChange={handleFile} />
          </div>
        )}

        {error && <div className="admin-error">{error}</div>}

        <div className="modal-actions">
          <button className="btn btn-primary" onClick={handleSave} disabled={saving} id="save-image-btn">
            {saving ? 'Saving…' : '💾 Save Photo'}
          </button>
          <button className="btn btn-secondary" onClick={onCancel}>Cancel</button>
        </div>
      </div>
    </div>
  )
}

export default function AdminDashboard() {
  const { seller } = useAuth()
  const navigate = useNavigate()
  const [products, setProducts] = useState([])
  const [categories, setCategories] = useState([])
  const [loading, setLoading] = useState(true)
  const [total, setTotal] = useState(0)
  const [search, setSearch] = useState('')
  const [activeCategory, setActiveCategory] = useState('')
  const [page, setPage] = useState(1)
  const [pages, setPages] = useState(1)
  const [toDelete, setToDelete] = useState(null)
  const [toEditImg, setToEditImg] = useState(null)
  const [toast, setToast] = useState(null)
  const searchRef = useRef()

  // Guard: redirect if not admin
  useEffect(() => {
    if (seller !== undefined && (!seller || !seller.is_admin)) {
      navigate('/')
    }
  }, [seller, navigate])

  const loadProducts = useCallback(async (q = '', cat = '', pg = 1) => {
    setLoading(true)
    try {
      const params = { page: pg, limit: 50 }
      if (q) params.search = q
      if (cat) params.category = cat
      const data = await adminFetchProducts(params)
      setProducts(data.items)
      setTotal(data.total)
      setPage(data.page)
      setPages(data.pages)
    } catch (err) {
      console.error(err)
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    fetchCategories().then(setCategories).catch(console.error)
    loadProducts()
  }, [loadProducts])

  const showToast = (msg, type = 'success') => {
    setToast({ msg, type })
    setTimeout(() => setToast(null), 3000)
  }

  const handleSearch = (e) => {
    e.preventDefault()
    setPage(1)
    loadProducts(search, activeCategory, 1)
  }

  const handleCategoryFilter = (slug) => {
    setActiveCategory(slug)
    setPage(1)
    loadProducts(search, slug, 1)
  }

  const handleDeleteConfirm = async () => {
    if (!toDelete) return
    try {
      await adminDeleteProduct(toDelete.id)
      setProducts((prev) => prev.filter((p) => p.id !== toDelete.id))
      setTotal((t) => t - 1)
      showToast(`"${toDelete.name}" deleted permanently.`, 'success')
    } catch (err) {
      showToast(err.response?.data?.detail || 'Delete failed.', 'error')
    } finally {
      setToDelete(null)
    }
  }

  const handleImageSaved = (updated) => {
    setProducts((prev) => prev.map((p) => (p.id === updated.id ? updated : p)))
    setToEditImg(null)
    showToast('Product photo updated!', 'success')
  }

  const imgSrc = (p) => p.image_url?.startsWith('http')
    ? p.image_url
    : `${API_BASE}${p.image_url}`

  if (!seller?.is_admin) return null

  return (
    <div className="admin-page">
      {/* Toast */}
      {toast && (
        <div className={`admin-toast ${toast.type}`}>
          {toast.type === 'success' ? '✅' : '❌'} {toast.msg}
        </div>
      )}

      {/* Delete confirm modal */}
      {toDelete && (
        <ConfirmModal
          product={toDelete}
          onConfirm={handleDeleteConfirm}
          onCancel={() => setToDelete(null)}
        />
      )}

      {/* Image edit modal */}
      {toEditImg && (
        <ImageEditModal
          product={toEditImg}
          onSave={handleImageSaved}
          onCancel={() => setToEditImg(null)}
        />
      )}

      <div className="container">
        {/* Header */}
        <div className="admin-header">
          <div className="admin-header-left">
            <div className="admin-badge">🛡️ Admin Panel</div>
            <h1 className="admin-title">Prionyx Shop Dashboard</h1>
            <p className="admin-sub">Full control over all marketplace products &amp; photos.</p>
          </div>
          <div className="admin-stats-row">
            <div className="admin-stat">
              <span className="admin-stat-val">{total}</span>
              <span className="admin-stat-lbl">Total Products</span>
            </div>
            <div className="admin-stat">
              <span className="admin-stat-val">{categories.length}</span>
              <span className="admin-stat-lbl">Categories</span>
            </div>
          </div>
        </div>

        {/* Filters */}
        <div className="admin-filters">
          <form className="admin-search-form" onSubmit={handleSearch}>
            <input
              ref={searchRef}
              className="form-input admin-search-input"
              type="text"
              placeholder="🔍 Search products, brands…"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              id="admin-search-input"
            />
            <button type="submit" className="btn btn-primary" id="admin-search-btn">Search</button>
            {(search || activeCategory) && (
              <button
                type="button"
                className="btn btn-secondary"
                onClick={() => { setSearch(''); setActiveCategory(''); loadProducts('', '', 1) }}
              >Clear</button>
            )}
          </form>

          <div className="admin-cat-filter">
            <button
              className={`admin-cat-chip ${!activeCategory ? 'active' : ''}`}
              onClick={() => handleCategoryFilter('')}
            >All</button>
            {categories.map((c) => (
              <button
                key={c.id}
                className={`admin-cat-chip ${activeCategory === c.slug ? 'active' : ''}`}
                onClick={() => handleCategoryFilter(c.slug)}
                id={`admin-cat-${c.slug}`}
              >
                {c.icon} {c.name}
              </button>
            ))}
          </div>
        </div>

        {/* Product table */}
        <div className="admin-table-wrap">
          {loading ? (
            <div className="admin-loading">
              <div className="spinner" style={{ width: 40, height: 40, borderWidth: 4 }} />
              <p>Loading products…</p>
            </div>
          ) : products.length === 0 ? (
            <div className="admin-empty">
              <div style={{ fontSize: '3rem' }}>🔍</div>
              <p>No products found.</p>
            </div>
          ) : (
            <table className="admin-table">
              <thead>
                <tr>
                  <th>Photo</th>
                  <th>Product</th>
                  <th>Brand</th>
                  <th>Category</th>
                  <th>Price</th>
                  <th>Stock</th>
                  <th>Seller</th>
                  <th>Actions</th>
                </tr>
              </thead>
              <tbody>
                {products.map((p) => (
                  <tr key={p.id} className="admin-table-row">
                    <td className="admin-td-img">
                      <div className="admin-img-wrap">
                        <img
                          src={imgSrc(p)}
                          alt={p.name}
                          className="admin-product-thumb"
                          onError={(e) => {
                            e.target.src = 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=100&q=60'
                          }}
                        />
                        <button
                          className="admin-img-edit-btn"
                          title="Edit photo"
                          onClick={() => setToEditImg(p)}
                          id={`edit-img-${p.id}`}
                        >✏️</button>
                      </div>
                    </td>
                    <td className="admin-td-name">
                      <a
                        href={`/products/${p.id}`}
                        target="_blank"
                        rel="noreferrer"
                        className="admin-product-link"
                      >
                        {p.name}
                      </a>
                      <div className="admin-product-id">ID #{p.id}</div>
                    </td>
                    <td className="admin-td-brand">{p.brand || '—'}</td>
                    <td className="admin-td-cat">
                      {p.category ? (
                        <span className="admin-cat-badge">
                          {p.category.icon} {p.category.name}
                        </span>
                      ) : '—'}
                    </td>
                    <td className="admin-td-price">{formatBDT(p.price_bdt)}</td>
                    <td className={`admin-td-stock ${p.stock === 0 ? 'out' : ''}`}>
                      {p.stock === 0 ? '⚠️ Out' : p.stock}
                    </td>
                    <td className="admin-td-seller">
                      {p.seller_shop_name || <span style={{ opacity: 0.4 }}>Seeded</span>}
                    </td>
                    <td className="admin-td-actions">
                      <button
                        className="btn btn-icon btn-photo"
                        title="Edit photo"
                        onClick={() => setToEditImg(p)}
                        id={`photo-btn-${p.id}`}
                      >🖼️</button>
                      <button
                        className="btn btn-icon btn-delete"
                        title="Delete product"
                        onClick={() => setToDelete(p)}
                        id={`delete-btn-${p.id}`}
                      >🗑️</button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>

        {/* Pagination */}
        {pages > 1 && (
          <div className="pagination" style={{ marginTop: '1.5rem' }}>
            <button className="btn btn-secondary" disabled={page <= 1}
              onClick={() => { const p = page - 1; setPage(p); loadProducts(search, activeCategory, p) }}>
              ← Prev
            </button>
            <span style={{ padding: '0 1rem', color: 'var(--text-secondary)' }}>
              Page {page} of {pages}
            </span>
            <button className="btn btn-secondary" disabled={page >= pages}
              onClick={() => { const p = page + 1; setPage(p); loadProducts(search, activeCategory, p) }}>
              Next →
            </button>
          </div>
        )}
      </div>
    </div>
  )
}
