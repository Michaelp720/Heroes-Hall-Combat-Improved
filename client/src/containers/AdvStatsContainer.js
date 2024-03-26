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


function AdvStatsContainer(){
    const { player, setPlayer } = useContext(PlayerContext)

    function advStat(stat){
        if (player['adv_points']>0){
            fetch(`/advstat/${player.id}`, {
                method: "PATCH",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                stat: stat
                })
            })
            .then(response => response.json())
            .then((player) => {
                setPlayer(player)
            })
        }
    }


    return (
        <Card width = {16}>
            <CardHeader as = 'h3' textAlign="center">Improve Stats (-1 AP)</CardHeader>
            <CardContent textAlign="center">
                <Button onClick = {() => advStat('max_hp')}>+3 HP</Button>
                <Button onClick = {() => advStat('base_pwr')}>+1 Pwr</Button>
                <br/>
                <br/>
                <Button onClick = {() => advStat('base_def')}>+1 Def</Button>
                <Button onClick = {() => advStat('spd')}>+2 Spd</Button>
            </CardContent>
        </Card>
    )}

export default AdvStatsContainer