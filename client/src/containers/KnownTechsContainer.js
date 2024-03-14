import React, { useEffect, useState, useContext } from "react";
import TechCard from "../components/TechCard"
import {PlayerContext} from '../context/player'
import {CombatContext} from '../context/combat'

function KnownTechsContainer({ character }){
    const { combat, setCombat } = useContext(CombatContext)
    const { player, setPlayer } = useContext(PlayerContext)

    //fetch characters known techs
    //fetch techs by tech_id for known_techs

    return(
        //TechCard for each knowntech- onclick useAction if character == player && if combat
        <div>
            <h1>KnownTechs</h1>
        </div>
    )

}

export default KnownTechsContainer