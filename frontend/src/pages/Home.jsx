import { useState, useEffect, useCallback } from 'react'
import { useNavigate } from 'react-router-dom'
import SearchBar from '../components/SearchBar'
import CategoryNav from '../components/CategoryNav'
import ProductGrid from '../components/ProductGrid'
import { fetchProducts } from '../api/client'
import './Home.css'

// Custom hook for fetching products
function useProducts() {
  const [products, setProducts] = useState([])
  const [loading, setLoading] = useState(true)
  const [total, setTotal] = useState(0)
  const [page, setPage] = useState(1)
  const [pages, setPages] = useState(1)
  const [filters, setFilters] = useState({})

  const load = useCallback(async (params = {}, pg = 1) => {
    setLoading(true)
    try {
      const cleaned = Object.fromEntries(
        Object.entries(params).filter(([, v]) => v !== undefined && v !== '')
      )
      const data = await fetchProducts({ ...cleaned, page: pg, limit: 20 })
      setProducts(data?.items || [])
      setTotal(data?.total || 0)
      setPage(data?.page || 1)
      setPages(data?.pages || 1)
    } catch (err) {
      console.error(err)
    } finally {
      setLoading(false)
    }
  }, [])

  return { products, loading, total, page, pages, filters, load, setFilters }
}

const HERO_CATEGORIES = [
  { icon: '📱', name: 'Smartphones', slug: 'smartphones', desc: '10 models' },
  { icon: '💻', name: 'Laptops', slug: 'laptops', desc: '10 models' },
  { icon: '🎧', name: 'Headphones', slug: 'headphones', desc: '10 models' },
  { icon: '📺', name: 'Smart TVs', slug: 'smart-tvs', desc: '10 models' },
  { icon: '📷', name: 'Cameras', slug: 'cameras', desc: '10 models' },
  { icon: '🎮', name: 'Gaming', slug: 'gaming', desc: '10 models' },
  { icon: '📲', name: 'Tablets', slug: 'tablets', desc: '10 models' },
  { icon: '⌚', name: 'Wearables', slug: 'wearables', desc: '10 models' },
  { icon: '🏠', name: 'Home Appliances', slug: 'home-appliances', desc: '10 models' },
  { icon: '🔌', name: 'Accessories', slug: 'accessories', desc: '10 models' },
]

export default function Home() {
  const navigate = useNavigate()
  const { products, loading, total, page, pages, filters, load, setFilters } = useProducts()
  const [activeCategory, setActiveCategory] = useState('')
  const [currentFilters, setCurrentFilters] = useState({})

  // Load products on mount
  useEffect(() => {
    load({})
  }, [load])

  const handleSearch = (searchParams) => {
    const merged = { ...activeCategory ? { category: activeCategory } : {}, ...searchParams }
    setCurrentFilters(searchParams)
    load(merged, 1)
  }

  const handleCategoryChange = (slug) => {
    setActiveCategory(slug)
    load({ ...currentFilters, category: slug || undefined }, 1)
  }

  const handleHeroCategoryClick = (slug) => {
    setActiveCategory(slug)
    load({ category: slug }, 1)
    document.getElementById('products-section')?.scrollIntoView({ behavior: 'smooth' })
  }

  const handlePageChange = (p) => {
    load({ ...currentFilters, category: activeCategory || undefined }, p)
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }

  return (
    <div className="home-page">
      {/* ── Hero ──────────────────────────────────────────────────────────── */}
      <section className="hero-section">
        <div className="hero-bg-orb orb-1" />
        <div className="hero-bg-orb orb-2" />
        <div className="hero-bg-orb orb-3" />
        <div className="container hero-content">
          <div className="hero-text">
            <div className="hero-badge">🇧🇩 Bangladesh's #1 Electronics Marketplace</div>
            <h1 className="hero-title">
              Find Your Next<br />
              <span className="hero-title-highlight">Tech Companion</span>
            </h1>
            <p className="hero-subtitle">
              Smartphones, laptops, gaming gear, wearables and more — at prices you'll love.
              Shop 100+ premium products across 10 categories with instant BDT &amp; USD pricing.
            </p>
          </div>
          <div className="hero-search-wrap">
            <SearchBar onSearch={handleSearch} />
          </div>
          {/* Category quick access */}
          <div className="hero-categories">
            {HERO_CATEGORIES.map((cat) => (
              <button
                key={cat.slug}
                className="hero-cat-btn"
                onClick={() => handleHeroCategoryClick(cat.slug)}
                id={`hero-cat-${cat.slug}`}
              >
                <span className="hero-cat-icon">{cat.icon}</span>
                <span className="hero-cat-name">{cat.name}</span>
                <span className="hero-cat-desc">{cat.desc}</span>
              </button>
            ))}
          </div>
        </div>
      </section>

      {/* ── Products ─────────────────────────────────────────────────────── */}
      <section className="products-section" id="products-section">
        <div className="container">
          <div className="section-header">
            <h2 className="section-title">
              {activeCategory
                ? HERO_CATEGORIES.find(c => c.slug === activeCategory)?.icon + ' ' +
                  HERO_CATEGORIES.find(c => c.slug === activeCategory)?.name
                : '✨ Featured Products'}
            </h2>
            {activeCategory && (
              <button
                className="btn btn-secondary btn-sm"
                onClick={() => handleCategoryChange('')}
              >
                View All →
              </button>
            )}
          </div>

          <CategoryNav activeSlug={activeCategory} onChange={handleCategoryChange} />

          <ProductGrid
            products={products}
            loading={loading}
            total={total}
            page={page}
            pages={pages}
            onPageChange={handlePageChange}
          />
        </div>
      </section>

      {/* ── Stats Banner ──────────────────────────────────────────────────── */}
      <section className="stats-section">
        <div className="container stats-grid">
          {[
            { icon: '📦', value: '100+', label: 'Products Listed' },
            { icon: '🏪', value: '10', label: 'Categories' },
            { icon: '⭐', value: '4.6', label: 'Avg. Rating' },
            { icon: '🇧🇩', value: 'BDT & USD', label: 'Dual Currency' },
          ].map((stat) => (
            <div key={stat.label} className="stat-item">
              <span className="stat-icon">{stat.icon}</span>
              <strong className="stat-value">{stat.value}</strong>
              <span className="stat-label">{stat.label}</span>
            </div>
          ))}
        </div>
      </section>
    </div>
  )
}
