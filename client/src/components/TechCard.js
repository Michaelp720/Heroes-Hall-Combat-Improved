import React, { useEffect, useState, useContext } from "react";
import {CombatContext} from '../context/combat'
import {PTurnContext} from '../context/playerturn'
import { Button, Segment, Header } from 'semantic-ui-react'

function TechCard({ techId }){
    const { combat, setCombat } = useContext(CombatContext)
    const [ tech, setTech ] = useState("")
    const { pturn, setPTurn } = useContext(PTurnContext)
    
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
        .then(data => setCombat(data))
        setPTurn(false)
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

    if (pturn) {
        return (
            <div>
                <h4>{tech.name}</h4>
                <Button onClick={chooseAction}>Use</Button>
            </div>
        );
    } else {
        return (
            <div>
                <h4>{tech.name}UH</h4>
            </div>
        );
}}

export default TechCard;