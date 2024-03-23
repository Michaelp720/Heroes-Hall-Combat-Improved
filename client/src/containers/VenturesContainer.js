//group of MonsterCards over a map
import React, { useEffect, useState } from "react";
import { Button, Segment, Header, CardMeta,
  CardHeader,
  CardDescription,
  CardContent,
  Card,
  Icon,
  Image, CardGroup} from 'semantic-ui-react'
import MonsterCard from "../components/MonsterCard"
import '../index.css'
import MapImage from "../images/FantasyMap.jpeg"

function VenturesContainer() {
  const [monsters, setMonsters] = useState([]);

  //fetch enemies- return monster card for each
  useEffect(() => {
    fetch(`/monsters`)
        .then(response => response.json())
        .then(data => setMonsters(data))
  }, [])

  return (
    //MonsterCard for each enemy
    <CardGroup itemsPerRow={4}
    style={{
      backgroundImage: `url(${MapImage})`,
      backgroundSize: 'cover', // Adjust as needed
      backgroundPosition: 'center', // Adjust as needed
      width: "800px"
    }}
  >
      {monsters.map((monster) => (
        <MonsterCard key = {monster['id']} monster = {monster}/>
      ))}
    </CardGroup>
  )
}

export default VenturesContainer;
