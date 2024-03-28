import React, { useEffect, useState, useContext } from "react";
import {PlayerContext} from '../context/player'
import {CombatContext} from '../context/combat'
import {PTurnContext} from '../context/playerturn'
//import {OpponentContext} from '../context/opponent'
import { useNavigate } from "react-router-dom";
import { Button, Segment, Header, CardMeta,
    CardHeader,
    CardDescription,
    CardContent,
    Card,
    Icon,
    Image, CardGroup} from 'semantic-ui-react'
import '../index.css'
  
//preview of Monster
//on click go to combat
// prop - {monster}
function MonsterCard({monster, size}) {
    const { player, setPlayer } = useContext(PlayerContext)
    const { combat, setCombat } = useContext(CombatContext)
    const { pturn, setPTurn } = useContext(PTurnContext)
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
            .then((newCombat) => {
                setCombat(newCombat);
                newCombat['player_next'] ? setPTurn(true) : setPTurn(false)
            })
            .then(() => {
                navigate("/combat")
            })

        // fetch(`/monsters/${monster.id}`)
        //     .then(response => response.json())
        //     .then(monster => setOpponent(monster))
    }
//<Image src = {monster.portrait} size = "mini" floated = "right"/>
    return (
        <Card raised = {true} size = "tiny">
            <CardHeader as = 'h4' textAlign="center">
                {monster.name}
            </CardHeader>
            
            <CardContent>Threat: {monster['threat_rating']}</CardContent>
            <Button onClick={startCombat}>
                Hunt
            </Button>
        </Card>
    )
  }
  
  export default MonsterCard;