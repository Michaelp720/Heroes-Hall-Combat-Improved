import React, { useEffect, useState, useContext } from "react";
import RoundCard from "../components/RoundCard"
import CharacterContainer from "../containers/CharacterContainer"
import {PTurnContext} from '../context/playerturn'
import StatusesContainer from "../containers/StatusesContainer"
import {CombatContext} from '../context/combat'
import { Button, Segment, Header } from 'semantic-ui-react'
import { useNavigate } from "react-router-dom";


function Combat() {
    const { combat, setCombat } = useContext(CombatContext)
    const { pturn, setPTurn } = useContext(PTurnContext)
    const navigate = useNavigate();
    
    function enemyAction(){
        //fetch and call get_player_action
        //response should be combat
        fetch(`/enemyaction`)
        .then(response => response.json())
        .then((combat) => {
            if(Object.keys(combat).length === 0){
                navigate("/ventures")
            }
            else{
                setCombat(combat);
                combat['player_next'] ? setPTurn(true) : setPTurn(false)
            }
        })
    }

    if (pturn) {
        return (
            <div>
                <RoundCard/>
                <StatusesContainer character={combat.player}/>
                <CharacterContainer character={combat.player}/>
                <StatusesContainer character={combat.enemy}/>
                <CharacterContainer character={combat.enemy}/>
            </div>
        );
    } else {
        return (
            <div>
                <RoundCard/>
                <Button onClick={enemyAction}>Monster Action</Button>
                <StatusesContainer character={combat.player}/>
                <CharacterContainer character={combat.player}/>
                <StatusesContainer character={combat.enemy}/>
                <CharacterContainer character={combat.enemy}/>
            </div>
        //round number
        //CharacterContainer passing combat.player as prop 
        //StatusesContainer passing combat.player
        //CharacterContainer passing combat.enemy as prop
        //StatusesContainer passing combat.enemy
        );
    }

  }
  
  export default Combat;