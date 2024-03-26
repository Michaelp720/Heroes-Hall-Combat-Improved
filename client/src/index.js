import React from "react";

import { PlayerProvider } from './context/player';
import { CombatProvider } from './context/combat';
import {OpponentProvider} from './context/opponent'
import {PTurnProvider} from './context/playerturn'
import ReactDOM from 'react-dom/client';
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import routes from "./routes.js";
import 'semantic-ui-css/semantic.min.css'
import './index.css'



const router = createBrowserRouter(routes);

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<PlayerProvider><CombatProvider><OpponentProvider><PTurnProvider><RouterProvider router={router} /></PTurnProvider></OpponentProvider> </CombatProvider> </PlayerProvider>);