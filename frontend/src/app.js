import React from 'react';
import ChatWindow from './components/chatwindow';
import './App.css'; // Assuming some global styling

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>AI Business Insights Co-Pilot</h1>
      </header>
      <main>
        {/* The main component for the chat interface */}
        <ChatWindow />
        
        {/* Placeholder for the real-time charts dashboard 
            You would add components here like:
            <SalesTrendChart />
            <TicketVolumeChart />
        */}
        <section className="dashboard-summary">
            <h2>Key Metrics Dashboard (Placeholder)</h2>
            <p>Static charts and visualizations based on /api/metrics endpoints will render here.</p>
        </section>
      </main>
      <footer>
        <p>&copy; 2025 AI Co-Pilot Project</p>
      </footer>
    </div>
  );
}

export default App;