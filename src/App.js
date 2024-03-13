import './App.css';
import React, { useState } from 'react';


function App() {
  const [tarotReading, setTarotReading] = useState(null);

  const fetchTarotReading = async () => {
    try {
      const response = await fetch('/api/tarot-reading'); 
      if (!response.ok) {
        console.log(response);
        throw new Error('Failed to fetch Tarot reading');
      }
      const data = await response.json();
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
        <button onClick={fetchTarotReading}>Choose your fate</button>
        {tarotReading && (
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
