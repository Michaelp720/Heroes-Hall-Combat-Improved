import React, { useEffect, useState, useContext } from "react";
import KnownTechsContainer from "./KnownTechsContainer"
import { Button, Segment, Header, CardMeta,
  CardHeader,
  CardDescription,
  CardContent,
  Card,
  Icon,
  Image, CardGroup} from 'semantic-ui-react'


//shows name, portrait, stat block
//stat block updates with statuses- stretch goal
//KnownTechsContainer with TechCards
//gets character as prop

//Fetches

function CharacterContainer({ character }) {
    
    let orderStr = ""

    if (character['order'] == 1){
      orderStr = "1st"
    }
    else{
      orderStr = "2nd"
    }
    
    

    return (
        //name, stat block
        //knowntechs container- pass character
      <Card>
        <CardHeader as= 'h1'> {character.name}</CardHeader>
        <Image src = {character.portrait} style={{ margin: '8px' }}/>
        <CardDescription as = 'h3'>HP: {character['crnt_hp']}/{character['max_hp']}</CardDescription>
        <CardMeta as = 'h3'>pwr: {character['temp_pwr']} | def: {character['temp_def']} | order: {orderStr}</CardMeta>
        <KnownTechsContainer character={character}/>
      </Card>
    )
  }
  
  export default CharacterContainer;