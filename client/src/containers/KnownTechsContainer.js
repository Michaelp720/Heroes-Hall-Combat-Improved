import React, { useEffect, useState, useContext } from "react";
import TechCard from "../components/TechCard"
import {PlayerContext} from '../context/player'
import {CombatContext} from '../context/combat'

function KnownTechsContainer({ character }){
    const { combat, setCombat } = useContext(CombatContext)
    const { player, setPlayer } = useContext(PlayerContext)
    let usable = false

    if (combat && (player.id == character.id)){
      usable = true
    }

    //fetch characters known techs
    //fetch techs by tech_id for known_techs
    
    function useTech(techId){
        fetch(`/action/${techId}`)
            .then(response => response.json())
    }

    if (usable) { //onClick = {() => useTech(techId)}
        return(
            <div>
                <h1>KnownTechs: usable</h1>
            </div>
        )
    }
    else{
        return(
        //TechCard for each knowntech- onclick useAction if character == player && if combat
            <div>
                <h1>KnownTechs: not usable</h1>
            </div>
        )
    }

}

export default KnownTechsContainer