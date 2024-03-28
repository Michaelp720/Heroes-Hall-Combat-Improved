import Landing from "./pages/Landing";
import Venture from "./pages/Venture";
import Guide from './pages/Guide'
import Login from './pages/Login';
import Combat from './pages/Combat';
import Advancement from './pages/Advancement';
import About from './pages/About'
import MonsterCard from "./components/MonsterCard";



const routes = [
    {
        path: "/",
        element: <Landing />,
    },
    {
        path: "/ventures",
        element: <Venture />,
    },
    {
        path: "/guide",
        element: <Guide />,
    },
    {
        path: "/login",
        element: <Login />,
    },
    {
        path: "/combat",
        element: <Combat />,
    },
    {
        path: "/monstertest",
        element: <MonsterCard />,
    },
    {
        path: "/advancement",
        element: <Advancement />,
    },
    {
        path: "/about",
        element: <About />,
    }
];

export default routes;