import ProductCard from './ProductCard'
import './ProductGrid.css'

function SkeletonCard() {
  return (
    <div className="product-card skeleton-card">
      <div className="skeleton skeleton-img" />
      <div className="skeleton-body">
        <div className="skeleton" style={{ height: 12, width: '50%' }} />
        <div className="skeleton" style={{ height: 16, width: '90%', marginTop: 8 }} />
        <div className="skeleton" style={{ height: 16, width: '70%', marginTop: 4 }} />
        <div className="skeleton" style={{ height: 22, width: '60%', marginTop: 12 }} />
        <div className="skeleton" style={{ height: 36, width: '100%', marginTop: 12, borderRadius: 10 }} />
      </div>
    </div>
  )
}

export default function ProductGrid({ products, loading, total, page, pages, onPageChange }) {
  if (loading) {
    return (
      <div className="product-grid">
        {[...Array(12)].map((_, i) => <SkeletonCard key={i} />)}
      </div>
    )
  }

  if (!loading && products.length === 0) {
    return (
      <div className="empty-state">
        <div className="empty-icon">🔍</div>
        <h3 className="empty-title">No products found</h3>
        <p className="empty-description">
          Try adjusting your search or budget filters to find what you're looking for.
        </p>
      </div>
    )
  }

  return (
    <div>
      {total != null && (
        <div className="results-meta">
          <span>{total.toLocaleString()} product{total !== 1 ? 's' : ''} found</span>
          {pages > 1 && <span>Page {page} of {pages}</span>}
        </div>
      )}

      <div className="product-grid">
        {products.map((p) => (
          <ProductCard key={p.id} product={p} />
        ))}
      </div>

      {/* Pagination */}
      {pages > 1 && (
        <div className="pagination">
          <button
            className="btn btn-secondary"
            disabled={page <= 1}
            onClick={() => onPageChange(page - 1)}
          >
            ← Prev
          </button>
          <div className="page-numbers">
            {[...Array(pages)].map((_, i) => {
              const p = i + 1
              if (p === 1 || p === pages || Math.abs(p - page) <= 2) {
                return (
                  <button
                    key={p}
                    className={`page-btn ${p === page ? 'active' : ''}`}
                    onClick={() => onPageChange(p)}
                  >
                    {p}
                  </button>
                )
              }
              if (Math.abs(p - page) === 3) return <span key={p} className="page-ellipsis">…</span>
              return null
            })}
          </div>
          <button
            className="btn btn-secondary"
            disabled={page >= pages}
            onClick={() => onPageChange(page + 1)}
          >
            Next →
          </button>
        </div>
      )}
    </div>
  )
}
