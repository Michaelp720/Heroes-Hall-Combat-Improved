import React, { useEffect, useState, useContext } from "react";
import TechCard from "../components/TechCard"
import {PlayerContext} from '../context/player'
import {CombatContext} from '../context/combat'
import { Button, Segment, Header } from 'semantic-ui-react'

function KnownTechsContainer({ character }){
    const { combat, setCombat } = useContext(CombatContext)
    const { player, setPlayer } = useContext(PlayerContext)

    const [ knownTechs, setKnownTechs ] = useState([])
    
    
    useEffect(() => {
        fetch(`/known_techs/${character['id']}`)
            .then(response => response.json())
            .then(data => setKnownTechs(data))
      }, [])

    return(
    <Segment>
      <Header as ='h3'>KnownTechs</Header>
      {knownTechs.map((knownTech) => (
        <TechCard key = {knownTech['id']} techId = {knownTech['tech_id']}/>
      ))}
    </Segment>
    )
}
export default KnownTechsContainer


//let usable = false

//     if (combat && (player.id == character.id)){
//       usable = true
//     }

//     //fetch characters known techs
//     //fetch techs by tech_id for known_techs
    
//     function chooseTechnique(techId, usable){
//         if (usable){        
//             fetch(`/action`, {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json",
//             },
//             body: JSON.stringify({
//                 actor: player,
//                 tech_id: techId,
//                 combat: combat
//             })
//         })}
//     }


//     const testTech = 1
//  //onClick = {() => useTech(techId)}
//     return(
//         <div>
//             <Button onClick = {() => chooseTechnique(testTech, usable)}>KnownTechs: usable</Button>
//         </div>
//     )

// }