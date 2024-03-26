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

    function navVenture(){
        navigate("/ventures")
    }

        return (

        <Grid columns={2} centered>
            <Grid.Row>
                <Grid.Column>
                    <Button onClick = {navHome}>Home</Button>
                    <Button onClick = {navVenture}>Adventure!</Button>
                </Grid.Column>
                <Grid.Column>
                    <Header as = 'h2' textAlign="left">Advancement</Header>
                </Grid.Column>
            </Grid.Row>
            <Grid.Row>
                <Grid.Column >
                    <CharacterContainer character={player} advancement = {true} />
                </Grid.Column>
        
                <Grid.Column width = {8}>
                    <AdvStatsContainer/>
                    <LrnTechsContainer/>
                </Grid.Column>
            </Grid.Row>
        </Grid>
    )}

export default Advancement