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
        <Card>
            <CardHeader as = 'h3' textAlign="center">Stats</CardHeader>
            <CardContent onClick = {() => advStat('max_hp')}>{player['max_hp']}</CardContent>
        </Card>
    )}

export default AdvStatsContainer