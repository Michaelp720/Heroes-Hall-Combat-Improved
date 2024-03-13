import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Landing from "./pages/Landing";
import VenturesContainer from './containers/VenturesContainer'
import About from './pages/About'
import Login from './pages/Login'
import "./index.css";
import { createRoot } from "react-dom/client";

const container = document.getElementById("root");
const root = createRoot(container);

root.render(
  <Router>
    <Switch>
      <Route exact path="/" component={Landing} />
      <Route exact path="/ventures" component={VenturesContainer} />
      <Route exact path="/about" component={About} />
      <Route exact path="/login" component={Login} />
    </Switch>
  </Router>
);