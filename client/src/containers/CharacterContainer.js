import React, { useEffect, useState, useContext } from "react";
import KnownTechsContainer from "./KnownTechsContainer"
import { Button, Segment, Header } from 'semantic-ui-react'


//shows name, portrait, stat block
//stat block updates with statuses- stretch goal
//KnownTechsContainer with TechCards
//gets character as prop

//Fetches

function CharacterContainer({ character }) {
    

    return (
        //name, stat block
        //knowntechs container- pass character
      <Segment>
        <Header as= 'h3'>{character.name}</Header>
        <Header as = 'h5'>HP: {character['crnt_hp']}/{character['max_hp']}</Header>
        <KnownTechsContainer character={character}/>
      </Segment>
    )
  }
  
  export default CharacterContainer;