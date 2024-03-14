import React, { useEffect, useState, useContext } from "react";
import {CombatContext} from '../context/combat'

//displays the current rnd
//fetch from combat

function RoundCard() {
    const { combat, setCombat } = useContext(CombatContext)

    return (
        <h1>Round: {combat.rnd}</h1>
    )
}

export default RoundCard