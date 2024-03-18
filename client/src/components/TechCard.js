import React, { useEffect, useState, useContext } from "react";
import {CombatContext} from '../context/combat'
import {PTurnContext} from '../context/playerturn'
import { Button, Segment, Header } from 'semantic-ui-react'
import { useNavigate } from "react-router-dom";

function TechCard({ techId, players_tech }){
    const { combat, setCombat } = useContext(CombatContext)
    const [ tech, setTech ] = useState("")
    const { pturn, setPTurn } = useContext(PTurnContext)
    const navigate = useNavigate();
    
    useEffect(() => {
        fetch(`/tech/${techId}`)
            .then(response => response.json())
            .then(data => setTech(data))
    }, [])

    function chooseAction(){
        //fetch and call get_player_action
        //response should be combat
        fetch(`/playeraction`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
            techId: techId
            })
        })
        .then(response => response.json())
        .then((combat) => {
            if(Object.keys(combat).length === 0){
                setPTurn(false)
                navigate("/ventures")
            }
            else {
                setCombat(combat);
                combat['player_next'] ? setPTurn(true) : setPTurn(false)
            }
        })
    }

    // return (
    //     <div>
    //         <h4>{tech.name}</h4>
    //         {pturn ? (
    //             <Button onClick={chooseAction}>Use</Button>
    //         ) : (
    //             <Button>Test</Button>
    //         )}
    //     </div>
    // );

    if (pturn && players_tech) {
        return (
            <div>
                <h4>{tech.name}</h4>
                <Button onClick={chooseAction}>Use</Button>
            </div>
        );
    } else {
        return (
            <div>
                <h4>{tech.name}</h4>
            </div>
        );
}}

export default TechCard;