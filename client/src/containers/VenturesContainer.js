//group of MonsterCards over a map
import React, { useEffect, useState } from "react";
import { Button, Segment, Header } from 'semantic-ui-react'
import MonsterCard from "../components/MonsterCard"

function VenturesContainer() {
  const [monsters, setMonsters] = useState([]);

  //fetch enemies- return monster card for each
  useEffect(() => {
    fetch(`/monsters`)
        .then(response => response.json())
        .then(data => setMonsters(data))
  }, [])

function handleClick(){
  console.log(monsters)
}

  return (
    //MonsterCard for each enemy
    <Segment>
      <Header as ='h2' onClick = {handleClick}>Ventures</Header>
      {monsters.map((monster) => (
        <MonsterCard monster = {monster}/>
      ))}
    </Segment>
  )
}

export default VenturesContainer;
