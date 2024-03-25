import React, { useEffect, useState, useContext } from "react";
import CharacterContainer from "../containers/CharacterContainer"
import VenturesContainer from "../containers/VenturesContainer"
import AdvStatsContainer from "../containers/AdvStatsContainer"
import LrnTechsContainer from "../containers/LrnTechsContainer"
import {PlayerContext} from '../context/player'
import {CombatContext} from '../context/combat'
import { Button, Segment, Header, CardMeta,
    CardHeader,
    CardDescription,
    CardContent,
    Card,
    Icon,
    Image, CardGroup, Grid} from 'semantic-ui-react'
    import { useNavigate } from "react-router-dom";


function Advancement(){
    const { player, setPlayer } = useContext(PlayerContext)
    const navigate = useNavigate();




    function navHome(){
        navigate("/")
    }

        return (
        <Segment>
            <Button onClick = {navHome}>Home</Button>
            <Header as = 'h2' textAlign="center">Advancement</Header>

            <CharacterContainer character={player} advancement = {true} />
            <AdvStatsContainer/>
            <LrnTechsContainer/>
        </Segment>
    )}

export default Advancement