import React, { useEffect, useState, useContext } from "react";
import {CombatContext} from '../context/combat'

//displays the current rnd
//fetch from combat

function RoundCard() {
    const { combat, setCombat } = useContext(CombatContext)

    function handleClick(){
        console.log(combat)
        console.log(combat['players_turn'])
    }

    return (
        <h1 onClick = {handleClick}>Round: {combat.rnd}</h1>
    )
}

export default RoundCard