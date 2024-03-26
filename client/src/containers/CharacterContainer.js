import React, { useEffect, useState, useContext } from "react";
import KnownTechsContainer from "./KnownTechsContainer"
import {PlayerContext} from '../context/player'
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

function CharacterContainer({ character, advancement = false }) {
    
    const { player, setPlayer } = useContext(PlayerContext)
    


    let orderStr = ""
    let orderSpdDisplay = ''

    

    let adv_display = ""

    if (advancement){
      adv_display = `Adv Points: ${character['adv_points']}`
      orderSpdDisplay = `spd: ${character['spd']}`
    }
    else {
      if (character['order'] == 1){
        orderStr = "1st"
      }
      else{
        orderStr = "2nd"
      }
      orderSpdDisplay = `order: ${orderStr}`
    }
    
    
    

    return (
        //name, stat block
        //knowntechs container- pass character
      <Card>
        <CardHeader as= 'h1'> {character.name}</CardHeader>
        <Image src = {character.portrait} style={{ margin: '8px' }}/>
        <CardDescription as = 'h3'>HP: {character['crnt_hp']}/{character['max_hp']}</CardDescription>
        <CardMeta as = 'h3'>pwr: {character['temp_pwr']} | def: {character['temp_def']} | {orderSpdDisplay}</CardMeta>
        <KnownTechsContainer character={character}/>
        <CardHeader as='h1'>
          {adv_display}
        </CardHeader>
      </Card>
    )
}
  
export default CharacterContainer;