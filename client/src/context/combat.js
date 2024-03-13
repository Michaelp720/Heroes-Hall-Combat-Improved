import { createContext, useState } from 'react';

const CombatContext = createContext()

function CombatProvider({ children }){
    const [combat, setCombat] = useState(null)

    return(
		<CombatContext.Provider value={{combat, setCombat}}>
			{children}
		</CombatContext.Provider>
	)
}

export { CombatContext, CombatProvider }

//import {CombatContext} from '../context/combat'

//const { combat, setCombat } = useContext(CombatContext)