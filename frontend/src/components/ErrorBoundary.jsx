import React from 'react'

export class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props)
    this.state = { hasError: false, error: null }
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error }
  }

  componentDidCatch(error, errorInfo) {
    console.error('ErrorBoundary caught an error:', error, errorInfo)
  }

  render() {
    if (this.state.hasError) {
      return (
        <div style={{ padding: '2rem', textAlign: 'center', color: '#ff4d4f' }}>
          <h2>Oops, something went wrong.</h2>
          <p>{this.state.error?.toString()}</p>
          <button 
            onClick={() => window.location.reload()}
            style={{ padding: '0.5rem 1rem', marginTop: '1rem', cursor: 'pointer', background: '#ff4d4f', color: '#fff', border: 'none', borderRadius: '4px' }}
          >
            Reload Page
          </button>
        </div>
      )
    }

    return this.props.children
  }
}
