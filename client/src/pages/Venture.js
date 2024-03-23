import React, { useEffect, useState, useContext } from "react";
import CharacterContainer from "../containers/CharacterContainer"
import VenturesContainer from "../containers/VenturesContainer"
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

//CharacterContainer for player
//VenturesContainer with MonsterCards

function Venture(){
    const { player, setPlayer } = useContext(PlayerContext)
    const { combat, setCombat } = useContext(CombatContext)
    const navigate = useNavigate();

    let outcomeMessage

    if (combat){
        if (combat['victor'] === "player"){
            outcomeMessage = `You were victorious! ${combat['enemy'][`name`]} was defeated`
        }
        else{
            outcomeMessage = `${player['name']} was defeated by ${combat['enemy'][`name`]}`
    }}


    function navHome(){
        navigate("/")
    }

        return (
        <Segment>
            <Button onClick = {navHome}>Home</Button>
            <Header as = 'h2' textAlign="center">{outcomeMessage}</Header>
            <Grid columns={2}>
                <Grid.Row>
                    <Grid.Column width = {4}>
                        <CharacterContainer character={player} />
                    </Grid.Column>
                    <Grid.Column>
                        <VenturesContainer />
                    </Grid.Column>
                </Grid.Row>
            </Grid>
        </Segment>
    )}

export default Venture