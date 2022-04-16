import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Info from './components/Info/index';


function App() {
  return (
    <Router>
      <Switch>
        <Route path="/info/:id" component={Info} />
      </Switch>
    </Router>

  );
}

export default App;
