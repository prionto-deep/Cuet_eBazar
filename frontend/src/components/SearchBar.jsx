import { useState } from 'react'
import './SearchBar.css'

const API_BASE = 'http://localhost:8000'
const MAX_PRICE_BDT = 500000

export default function SearchBar({ onSearch, initialValues = {} }) {
  const [query, setQuery] = useState(initialValues.search || '')
  const [minPrice, setMinPrice] = useState(initialValues.min_price || '')
  const [maxPrice, setMaxPrice] = useState(initialValues.max_price || '')
  const [showBudget, setShowBudget] = useState(false)

  const handleSubmit = (e) => {
    e.preventDefault()
    onSearch({
      search: query.trim() || undefined,
      min_price: minPrice ? Number(minPrice) : undefined,
      max_price: maxPrice ? Number(maxPrice) : undefined,
    })
  }

  const handleClear = () => {
    setQuery('')
    setMinPrice('')
    setMaxPrice('')
    onSearch({})
  }

  const usd = (bdt) => bdt ? `~$${(Number(bdt) / 110).toFixed(0)}` : ''

  return (
    <form className="search-bar-form" onSubmit={handleSubmit} id="search-form">
      <div className="search-main-row">
        {/* Search input */}
        <div className="search-input-wrap">
          <span className="search-icon">🔍</span>
          <input
            type="text"
            className="search-input"
            placeholder="Search for smartphones, laptops, cameras..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            id="search-input"
          />
          {query && (
            <button
              type="button"
              className="search-clear"
              onClick={() => setQuery('')}
              aria-label="Clear search"
            >✕</button>
          )}
        </div>

        {/* Budget toggle */}
        <button
          type="button"
          className={`budget-toggle-btn ${showBudget ? 'active' : ''}`}
          onClick={() => setShowBudget(!showBudget)}
          id="budget-toggle-btn"
        >
          💰 Budget
          {(minPrice || maxPrice) && (
            <span className="budget-indicator">●</span>
          )}
        </button>

        {/* Search button */}
        <button type="submit" className="btn btn-primary search-submit-btn" id="search-submit-btn">
          Search
        </button>
      </div>

      {/* Budget panel */}
      {showBudget && (
        <div className="budget-panel fade-in-up">
          <div className="budget-label-row">
            <span className="budget-title">💵 Budget Filter</span>
            {(minPrice || maxPrice) && (
              <button type="button" className="budget-reset" onClick={() => { setMinPrice(''); setMaxPrice(''); }}>
                Reset
              </button>
            )}
          </div>
          <div className="budget-inputs">
            <div className="budget-field">
              <label htmlFor="min-price-input">Min Price (৳)</label>
              <div className="price-input-wrap">
                <span className="price-symbol">৳</span>
                <input
                  type="number"
                  id="min-price-input"
                  className="form-input price-input"
                  placeholder="0"
                  value={minPrice}
                  onChange={(e) => setMinPrice(e.target.value)}
                  min={0}
                />
              </div>
              {minPrice && <span className="usd-hint">{usd(minPrice)} USD</span>}
            </div>

            <div className="budget-separator">—</div>

            <div className="budget-field">
              <label htmlFor="max-price-input">Max Price (৳)</label>
              <div className="price-input-wrap">
                <span className="price-symbol">৳</span>
                <input
                  type="number"
                  id="max-price-input"
                  className="form-input price-input"
                  placeholder="500,000"
                  value={maxPrice}
                  onChange={(e) => setMaxPrice(e.target.value)}
                  min={0}
                />
              </div>
              {maxPrice && <span className="usd-hint">{usd(maxPrice)} USD</span>}
            </div>
          </div>

          {/* Quick budget presets */}
          <div className="budget-presets">
            <span className="presets-label">Quick select:</span>
            {[
              { label: 'Under ৳10K', max: 10000 },
              { label: '৳10K–50K', min: 10000, max: 50000 },
              { label: '৳50K–150K', min: 50000, max: 150000 },
              { label: 'Above ৳150K', min: 150000 },
            ].map((p) => (
              <button
                key={p.label}
                type="button"
                className="preset-btn"
                onClick={() => {
                  setMinPrice(p.min || '')
                  setMaxPrice(p.max || '')
                }}
              >
                {p.label}
              </button>
            ))}
          </div>
        </div>
      )}
    </form>
  )
}
