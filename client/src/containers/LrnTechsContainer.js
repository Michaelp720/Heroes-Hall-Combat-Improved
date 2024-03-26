import React, { useEffect, useState, useContext } from "react";
import TechCard from "../components/TechCard"
import {PlayerContext} from '../context/player'
import { Button, Segment, Header, CardMeta,
    CardHeader,
    CardDescription,
    CardContent,
    Card,
    Icon,
    Image, CardGroup, Grid} from 'semantic-ui-react'


function LrnTechsContainer(){
    const { player, setPlayer } = useContext(PlayerContext)
    const [unlockedTechs, setUnlockedTechs] = useState([])
    
    useEffect(() => {
        fetch(`/unlockedtechs/${player['id']}`)
            .then(response => response.json())
            .then(data => setUnlockedTechs(data))
    }, [player])

    function handleClick(){
        console.log(unlockedTechs)
    }

    return (
        <CardGroup>
            <CardHeader as = 'h3' textAlign="center" onClick = {handleClick}>Techs</CardHeader>
            {unlockedTechs.map((unlockedTech) => (
                <TechCard key = {unlockedTech['id']} techId = {unlockedTech['id']} players_tech = {true} adv = {true}/>
            ))}
        </CardGroup>
    )}

export default LrnTechsContainer