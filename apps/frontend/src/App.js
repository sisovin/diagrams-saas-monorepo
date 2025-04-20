import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Analytics from './pages/Analytics';
import Auth from './pages/Auth';
import Chat from './pages/Chat';
import CRM from './pages/CRM';
import Files from './pages/Files';
import Generic from './pages/Generic';
import Identity from './pages/Identity';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/analytics" component={Analytics} />
        <Route path="/auth" component={Auth} />
        <Route path="/chat" component={Chat} />
        <Route path="/crm" component={CRM} />
        <Route path="/files" component={Files} />
        <Route path="/generic" component={Generic} />
        <Route path="/identity" component={Identity} />
      </Switch>
    </Router>
  );
}

export default App;
