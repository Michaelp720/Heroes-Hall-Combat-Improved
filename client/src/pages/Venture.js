import React, { useEffect, useState, useContext } from "react";
import CharacterContainer from "../containers/CharacterContainer"
import VenturesContainer from "../containers/VenturesContainer"
import {PlayerContext} from '../context/player'

//CharacterContainer for player
//VenturesContainer with MonsterCards

function Venture(){
    const { player, setPlayer } = useContext(PlayerContext)

}

export default Venture