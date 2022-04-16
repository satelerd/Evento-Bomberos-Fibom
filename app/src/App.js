// import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Info from './components/Info/index';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/:id" element={<Info />} exact />
      </Routes>
    </Router>


  );
}


export default App;
