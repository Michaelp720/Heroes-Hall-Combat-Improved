import React, { useEffect, useState, useContext } from "react";
import {PlayerContext} from '../context/player'
import {CombatContext} from '../context/combat'
import { useNavigate } from "react-router-dom";
//preview of Monster
//on click go to combat
// prop - {monster}
function MonsterCard({monster}) {
    const { player, setPlayer } = useContext(PlayerContext)
    const { combat, setCombat } = useContext(CombatContext)
    const navigate = useNavigate();
    //monster is an Enemy object
    //on click post combat with player and monster, then navigate to combat page
    
    //testing
    //const player = {id:1}
    //const monster = {id:2}

    function startCombat(){
        fetch(`/combat/${player.id}/${monster.id}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify()
        })
            .then((response => response.json()))
            .then((newCombat) => setCombat(newCombat))
            .then(() => {
                navigate("/combat")
            })
    }

    return (
        <div>
            <h1 onClick={startCombat}>MonsterCard</h1>
        </div>
    )
  }
  
  export default MonsterCard;