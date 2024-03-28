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
import MapImage from "../images/Baleweld.webp"

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
    <CardGroup size = "tiny" itemsPerRow={4}>
      {monsters.map((monster) => (
        <MonsterCard key = {monster['id']} monster = {monster}/>
      ))}
    </CardGroup>
  )
}

export default VenturesContainer;
