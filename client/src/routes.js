import Landing from "./pages/Landing";
import Venture from "./pages/Venture";
import Guide from './pages/Guide'
import Login from './pages/Login';
import Combat from './pages/Combat';
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
    }
];

export default routes;