import { createContext, useState } from 'react';

const PlayerContext = createContext()

function PlayerProvider({ children }){
    const [player, setPlayer] = useState(null)

    return(
		<PlayerContext.Provider value={{player, setPlayer}}>
			{children}
		</PlayerContext.Provider>
	)
}

export { PlayerContext, PlayerProvider }

//import {PlayerContext} from '../context/player'

//const { player, setPlayer } = useContext(PlayerContext)