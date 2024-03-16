import React, { useEffect, useState, useContext } from "react";
import CharacterContainer from "../containers/CharacterContainer"
import VenturesContainer from "../containers/VenturesContainer"
import {PlayerContext} from '../context/player'
import { Segment, Header } from 'semantic-ui-react'

//CharacterContainer for player
//VenturesContainer with MonsterCards

function Venture(){
    const { player, setPlayer } = useContext(PlayerContext)


    return (
        <Segment>
            <CharacterContainer character = {player}/>
            <VenturesContainer/>
        </Segment>
    )
}

export default Venture