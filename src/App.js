import './App.css';
import React, { useState } from 'react';


function App() {
  const [tarotReading, setTarotReading] = useState(null);
  const [loading, setLoading] = useState(false)


  const fetchTarotReadingLove = async () => {
    
    try {
      setLoading(true);
      const response = await fetch('/api/tarot-reading', {method: "GET", headers: {"Content-Type": "my love life"}}); 
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
  const fetchTarotReadingCareer = async () => {
    
    try {
      setLoading(true);
      const response = await fetch('/api/tarot-reading', {method: "GET", headers: {"Content-Type": "my career"}}); 
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
  const fetchTarotReadingFuture = async () => {
    
    try {
      setLoading(true);
      const response = await fetch('/api/tarot-reading', {method: "GET", headers: {"Content-Type": "my future"}}); 
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
        <a><small>What would you like a reading on today?</small></a>
        <br/>
        <button onClick={fetchTarotReadingLove} disabled={loading}>
          Love
          </button>
          <button onClick={fetchTarotReadingCareer} disabled={loading}>
          Career
          </button>
          <button onClick={fetchTarotReadingFuture} disabled={loading}>
          Future
          </button>
        
        {loading ? <div> <br></br> <a>Please allow up to five minutes to receive your reading...</a> <img src = {"https://i.pinimg.com/originals/fb/f4/b4/fbf4b4b5b982c142d6b25d8bf45daa40.gif"} alt="loading..." /> </div>: tarotReading && (
          <div className="Tarot-Reading">
            <h2><b>Your Tarot Reading</b></h2>
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
        <br/>
        <a href="http://fathomless-bayou-60027.herokuapp.com/"><small>By Jerard Louis Dayanghirang Guevarra
        <br/>
        Click here to find me online!
        </small></a>
      </header>
      
    </div>
  );
}

export default App;
