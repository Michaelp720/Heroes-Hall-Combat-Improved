import React, { useEffect, useState, useContext } from "react";
import RoundCard from "../components/RoundCard"
import CharacterContainer from "../containers/CharacterContainer"
import StatusesContainer from "../containers/StatusesContainer"
import {CombatContext} from '../context/combat'

//CharacterContainer for player, CharacterContainer for enemy, 
//StatusesContainer for player and enemy with StatusCards
//RoundCard

//Fetches

//State- player character


function Combat() {
    const { combat, setCombat } = useContext(CombatContext)

    


    return (
        //round number
        //CharacterContainer passing combat.player as prop 
        //StatusesContainer passing combat.player
        //CharacterContainer passing combat.enemy as prop
        //StatusesContainer passing combat.enemy
        <div>
            <RoundCard/>
            <CharacterContainer character={combat.player}/>
            <CharacterContainer character={combat.enemy}/>
        </div>
    )
  }
  
  export default Combat;