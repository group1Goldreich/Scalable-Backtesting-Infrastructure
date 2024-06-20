import React from 'react';
import Navbar from './components/Navbar';
import BacktestForm from './components/BacktestForm';

function App() {
  return (
    <div className="App">
      <Navbar />
      <div className="container mx-auto p-4">
        <BacktestForm />
      </div>
    </div>
  );
}

export default App;
