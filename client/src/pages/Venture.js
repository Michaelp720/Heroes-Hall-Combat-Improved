import React, { useEffect, useState, useContext } from "react";
import CharacterContainer from "../containers/CharacterContainer"
import VenturesContainer from "../containers/VenturesContainer"
import {PlayerContext} from '../context/player'
import { Button, Segment, Header, CardMeta,
    CardHeader,
    CardDescription,
    CardContent,
    Card,
    Icon,
    Image, CardGroup} from 'semantic-ui-react'

//CharacterContainer for player
//VenturesContainer with MonsterCards

function Venture(){
    const { player, setPlayer } = useContext(PlayerContext)


    return (
        <CardGroup>
            <CharacterContainer character = {player}/>
            <VenturesContainer/>
        </CardGroup>
    )
}

export default Venture