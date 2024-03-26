import React, { useEffect, useState, useContext } from "react";
import TechCard from "../components/TechCard"
import {PlayerContext} from '../context/player'
import {CombatContext} from '../context/combat'
import { Button, Segment, Header, CardMeta,
  CardHeader,
  CardDescription,
  CardContent,
  Card,
  Icon,
  Image, CardGroup} from 'semantic-ui-react'

function KnownTechsContainer({ character }){
    const { combat, setCombat } = useContext(CombatContext)
    const { player, setPlayer } = useContext(PlayerContext)

    const [ knownTechs, setKnownTechs ] = useState([])
    
    let players_tech = false

    if (character['id'] == player['id']){
      players_tech = true
    }
    
    useEffect(() => {
        fetch(`/known_techs/${character['id']}`)
            .then(response => response.json())
            .then(data => setKnownTechs(data))
      }, [player])

    return(
    <CardGroup itemsPerRow={2}>
      {knownTechs.map((knownTech) => (
        <TechCard key = {knownTech['id']} techId = {knownTech['tech_id']} players_tech = {players_tech}/>
      ))}
    </CardGroup>
    )
}
export default KnownTechsContainer
