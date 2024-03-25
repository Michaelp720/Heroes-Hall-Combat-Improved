import React, { useEffect, useState, useContext } from "react";
import {CombatContext} from '../context/combat'
import {PTurnContext} from '../context/playerturn'
import { Button, Segment, Header, CardMeta,
    CardHeader,
    CardDescription,
    CardContent,
    Card,
    Icon,
    Image, CardGroup} from 'semantic-ui-react'
import { useNavigate } from "react-router-dom";
import '../index.css'

function TechCard({ techId, players_tech, adv = false }){
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
        fetch(`/playeraction/${techId}`, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
            techId: techId
            })
        })
        .then(response => response.json())
        .then((combat) => {
            if(combat.victor){
                setPTurn(false)
                setCombat(combat)
                navigate("/ventures")
            }
            else {
                setCombat(combat);
                combat['player_next'] ? setPTurn(true) : setPTurn(false)
            }
        })
    }

    let techDescription = ''

    if (tech.target == "opponent"){
        if (tech.stat == 'hp'){
            techDescription = "dmg target"
        }
        else{
            techDescription = `reduces ${tech.stat}`
        }
    }
    else{
        if (tech.stat == 'hp'){
            techDescription = `heal self`
        }
        else{
            techDescription = `buffs ${tech.stat}`
        }
    }

    if (pturn && players_tech) {
        return (
            <Card>
                <CardDescription textAlign="center" as = 'h4'>____{tech.name}____</CardDescription>
                <CardDescription>| {techDescription}</CardDescription>
                <Button onClick={chooseAction}>Use</Button>
            </Card>
        );
    } else {
        return (
            <Card>
                <CardHeader textAlign="center" as = 'h4'>____{tech.name}____</CardHeader>
                <CardDescription>| {techDescription}</CardDescription>
            </Card>
        );
}}

export default TechCard;