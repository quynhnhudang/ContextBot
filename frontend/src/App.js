import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [message, setMessage] = useState('');
  const [chat, setChat] = useState([]);
  const [context, setContext] = useState('');

  const handleSend = async () => {
    const userMessage = { sender: 'user', text: message };
    setChat([...chat, userMessage]);
    setMessage('');

    const response = await axios.post('/chat', {
      message,
      context
    });

    const botMessage = { sender: 'bot', text: response.data.response };
    setChat([...chat, userMessage, botMessage]);
    setContext(response.data.context);
  };

  return (
    <div className="App">
      <div className="chat-box">
        {chat.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
      </div>
      <input 
        type="text" 
        value={message} 
        onChange={(e) => setMessage(e.target.value)} 
        placeholder="Type a message..." 
      />
      <button onClick={handleSend}>Send</button>
    </div>
  );
}

export default App;
