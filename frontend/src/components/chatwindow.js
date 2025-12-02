import React, { useState } from 'react';
import { fetchInsight } from '../api';
import './ChatWindow.css'; // Add basic styling

const ChatWindow = () => {
  const [messages, setMessages] = useState([
    { sender: 'AI', text: "Hello! I'm your Business Insights Co-Pilot. Ask me anything about Sales, Tickets, or Users." }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSend = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userQuery = input.trim();
    setMessages(prev => [...prev, { sender: 'User', text: userQuery }]);
    setInput('');
    setIsLoading(true);

    try {
      const insight = await fetchInsight(userQuery);
      setMessages(prev => [...prev, { sender: 'AI', text: insight }]);
    } catch (error) {
      setMessages(prev => [...prev, { sender: 'AI', text: `Error: ${error.message}` }]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <h2>📊 AI Business Co-Pilot</h2>
      <div className="message-list">
        {messages.map((msg, index) => (
          <div key={index} className={`message-bubble ${msg.sender.toLowerCase()}`}>
            <strong>{msg.sender}:</strong> {msg.text}
          </div>
        ))}
        {isLoading && <div className="loading-message">AI Co-Pilot is thinking...</div>}
      </div>
      <form onSubmit={handleSend} className="input-form">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="e.g., What was our total revenue last quarter?"
          disabled={isLoading}
        />
        <button type="submit" disabled={isLoading}>Send</button>
      </form>
    </div>
  );
};

export default ChatWindow;