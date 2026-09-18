import { useState, useEffect } from 'react'
import { fetchCategories } from '../api/client'
import './CategoryNav.css'

const ALL_CATEGORY = { id: null, name: 'All', slug: '', icon: '🛍️' }

export default function CategoryNav({ activeSlug, onChange }) {
  const [categories, setCategories] = useState([ALL_CATEGORY])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchCategories()
      .then((cats) => setCategories([ALL_CATEGORY, ...cats]))
      .catch(console.error)
      .finally(() => setLoading(false))
  }, [])

  if (loading) {
    return (
      <div className="category-nav">
        {[...Array(6)].map((_, i) => (
          <div key={i} className="category-chip skeleton" style={{ width: 100, height: 44 }} />
        ))}
      </div>
    )
  }

  return (
    <div className="category-nav-wrapper">
      <div className="category-nav">
        {categories.map((cat) => {
          const isActive = cat.slug === (activeSlug || '')
          return (
            <button
              key={cat.id ?? 'all'}
              className={`category-chip ${isActive ? 'active' : ''}`}
              onClick={() => onChange(cat.slug)}
              id={`category-chip-${cat.slug || 'all'}`}
            >
              <span className="chip-icon">{cat.icon}</span>
              <span className="chip-label">{cat.name}</span>
            </button>
          )
        })}
      </div>
    </div>
  )
}
