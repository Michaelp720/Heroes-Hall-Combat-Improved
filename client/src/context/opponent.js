import { createContext, useState } from 'react';

const OpponentContext = createContext()

function OpponentProvider({ children }){
    const [opponent, setOpponent] = useState(null)

    return(
		<OpponentContext.Provider value={{opponent, setOpponent}}>
			{children}
		</OpponentContext.Provider>
	)
}

export { OpponentContext, OpponentProvider }

//import {OpponentContext} from '../context/opponent'

//const { opponent, setOpponent } = useContext(OpponentContext)