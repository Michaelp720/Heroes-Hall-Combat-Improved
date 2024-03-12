// import React from "react";
// import App from "./components/App";
// import "./index.css";
// import { createRoot } from "react-dom/client";

// const container = document.getElementById("root");
// const root = createRoot(container);
// root.render(<App />);


import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Home from "./components/Home";
import VenturesContainer from './containers/VenturesContainer'
import "./index.css";
import { createRoot } from "react-dom/client";

const container = document.getElementById("root");
const root = createRoot(container);

root.render(
  <Router>
    <Switch>
      <Route exact path="/" component={Home} />
      <Route exact path="/ventures" component={VenturesContainer} />
    </Switch>
  </Router>
);