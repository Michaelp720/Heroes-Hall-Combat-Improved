import { createContext, useState } from 'react';

const PTurnContext = createContext()

function PTurnProvider({ children }){
    const [pturn, setPTurn] = useState(null)

    return(
		<PTurnContext.Provider value={{pturn, setPTurn}}>
			{children}
		</PTurnContext.Provider>
	)
}

export { PTurnContext, PTurnProvider }

//import {PTurnContext} from '../context/playerturn'

//const { pturn, setPTurn } = useContext(PTurnContext)