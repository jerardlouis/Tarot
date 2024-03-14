import './App.css';
import React, { useState } from 'react';


function App() {
  const [tarotReading, setTarotReading] = useState(null);
  const [loading, setLoading] = useState(false)


  const fetchTarotReading = async () => {
    try {
      setLoading(true);
      const response = await fetch('/api/tarot-reading'); 
      if (!response.ok) {
        console.log(response);
        throw new Error('Failed to fetch Tarot reading');
      }
      const data = await response.json();
      setLoading(false);
      setTarotReading(data);
      console.log(data);
    } catch (error) {
      console.error('Error fetching Tarot reading:', error);
    }
  };


  return (
    <div className="App">
      <header className="App-header">
        <img src={"https://cdn11.bigcommerce.com/s-e62be/images/stencil/1280x1280/products/6749/11202/Midori091219-129__76162.1571069617.jpg?c=2"} className="App-logo" alt="logo" />
        <p>
          Welcome to TarotAI
        </p>
        <button onClick={fetchTarotReading} disabled={loading}>
          Choose your fate
          </button>
        
        {loading ? <img src = {"https://i.pinimg.com/originals/fb/f4/b4/fbf4b4b5b982c142d6b25d8bf45daa40.gif"} alt="loading..." /> : tarotReading && (
          <div className="Tarot-Reading">
            <h2>Your Tarot Reading</h2>
            <ul>
              {tarotReading.cards.map((card, index) => (
                <li key={index}>
                  <strong>Card:</strong> {card} 
                  <strong> Orientation:</strong> {tarotReading.reversed[index]}  <br />
                </li>
              ))}
            </ul>
            AI Interpretation: <br />
            <small>{tarotReading.reading}</small>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
