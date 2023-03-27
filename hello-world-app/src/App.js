import React, { useState } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState('');

  const handleClick = () => {
    fetch('/hello')
      .then(response => response.json())
      .then(data => setMessage(data.message));
  };

  return (
    <div className="App">
      <button onClick={handleClick}>Hello World</button>
      <p>{message}</p>
    </div>
  );
}

export default App;
r