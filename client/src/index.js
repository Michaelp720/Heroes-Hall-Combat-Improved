import React from "react";

import { PlayerProvider } from './context/player';
import { CombatProvider } from './context/combat';
import {OpponentProvider} from './context/opponent'
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import routes from "./routes.js";
import 'semantic-ui-css/semantic.min.css'



const router = createBrowserRouter(routes);

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<PlayerProvider><CombatProvider><OpponentProvider><RouterProvider router={router} /></OpponentProvider> </CombatProvider> </PlayerProvider>);