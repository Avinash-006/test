import { useState } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [a, setA] = useState('')
  const [b, setB] = useState('')
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)

  const calculate = async (operation) => {
    try {
      const response = await axios.post(`http://127.0.0.1:8000/${operation}/`, {
        a: parseFloat(a),
        b: parseFloat(b)
      })
      setResult(response.data.result)
      setError(null)
    } catch (err) {
      setResult(null)
      setError(err.response?.data?.error || "Server Error")
    }
  }

  return (
    <div className="App">
      <h1>Django Calculator (POST)</h1>

      <input
        type="number"
        placeholder="Enter A"
        value={a}
        onChange={(e) => setA(e.target.value)}
      />
      <input
        type="number"
        placeholder="Enter B"
        value={b}
        onChange={(e) => setB(e.target.value)}
      />

      <div style={{ marginTop: '10px' }}>
        <button onClick={() => calculate('add')}>➕ Add</button>
        <button onClick={() => calculate('subtract')}>➖ Subtract</button>
        <button onClick={() => calculate('multiply')}>✖️ Multiply</button>
        <button onClick={() => calculate('divide')}>➗ Divide</button>
      </div>

      {result !== null && (
        <h2 style={{ color: 'green' }}>Result: {result}</h2>
      )}
      {error && (
        <h2 style={{ color: 'red' }}>Error: {error}</h2>
      )}
    </div>
  )
}

export default App
