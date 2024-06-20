import React from 'react';
import Navbar from './components/Navbar';
import BacktestForm from './components/BacktestForm';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Signup from './components/Signup';
import Login from './components/Login';
function App() {
  return (
    <Router>

    <div className="App">
      <Navbar />
      <div className="container mx-auto p-4">
      <Routes>
            <Route path="/" element={<BacktestForm />} />
            <Route path="/signup" element={<Signup />} />
            <Route path="/login" element={<Login />} />
          </Routes>
      </div>
    </div>
    </Router>
  );
}

export default App;
