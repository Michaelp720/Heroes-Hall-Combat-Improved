import React, { useEffect, useState, useContext } from "react";
import CharacterContainer from "../containers/CharacterContainer"
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
    


    return (
        <Card>
            <CardHeader as = 'h3' textAlign="center">Techs</CardHeader>
            <CardContent onClick = {() => advStat('max_hp')}>{player['max_hp']}</CardContent>
        </Card>
    )}

export default LrnTechsContainer