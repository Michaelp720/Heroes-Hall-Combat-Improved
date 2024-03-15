import React, { useEffect, useState, useContext } from "react";
import {PlayerContext} from '../context/player'
import {CombatContext} from '../context/combat'
//import {OpponentContext} from '../context/opponent'
import { useNavigate } from "react-router-dom";
import { Button, Segment, Header } from 'semantic-ui-react'
//preview of Monster
//on click go to combat
// prop - {monster}
function MonsterCard({monster}) {
    const { player, setPlayer } = useContext(PlayerContext)
    const { combat, setCombat } = useContext(CombatContext)
    //const { opponent, setOpponent } = useContext(OpponentContext)
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

        // fetch(`/monsters/${monster.id}`)
        //     .then(response => response.json())
        //     .then(monster => setOpponent(monster))
    }

    return (
        <Header as = 'h3' onClick={startCombat}>{monster.name}</Header>
    )
  }
  
  export default MonsterCard;