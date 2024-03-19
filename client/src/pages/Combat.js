import React, { useEffect, useState, useContext } from "react";
import RoundCard from "../components/RoundCard"
import CharacterContainer from "../containers/CharacterContainer"
import {PTurnContext} from '../context/playerturn'
import StatusesContainer from "../containers/StatusesContainer"
import {CombatContext} from '../context/combat'
import { Button, Segment, Header, CardMeta,
    CardHeader,
    CardDescription,
    CardContent,
    Card,
    Icon,
    Image, CardGroup} from 'semantic-ui-react'
import { useNavigate } from "react-router-dom";
import '../index.css'

    // <Card>
    //   <Image src='/images/avatar/large/matthew.png' wrapped ui={false} />
    //   <CardContent>
    //     <CardHeader>Matthew</CardHeader>
    //     <CardMeta>
    //       <span className='date'>Joined in 2015</span>
    //     </CardMeta>
    //     <CardDescription>
    //       Matthew is a musician living in Nashville.
    //     </CardDescription>
    //   </CardContent>
    //   <CardContent extra>
    //     <a>
    //       <Icon name='user' />
    //       22 Friends
    //     </a>
    //   </CardContent>
    // </Card>



function Combat() {
    const { combat, setCombat } = useContext(CombatContext)
    const { pturn, setPTurn } = useContext(PTurnContext)
    const navigate = useNavigate();
    
    function enemyAction(){
        //fetch and call get_player_action
        //response should be combat
        fetch(`/enemyaction`)
        .then(response => response.json())
        .then((combat) => {
            if(Object.keys(combat).length === 0){
                navigate("/ventures")
            }
            else{
                setCombat(combat);
                console.log(combat);
                combat['player_next'] ? setPTurn(true) : setPTurn(false)
            }
        })
    }

    if (pturn) {
        return (
            <Segment>
            <CardGroup itemsPerRow={3}>
                <Card>
                    <StatusesContainer character={combat.player}/>
                </Card>
                <Button className="button-fixed-width" style={{ fontSize: '20px' }}>Round: {combat.rnd}
                <br/>
                <br/>
                {combat.player.name}'s Turn</Button>
                <Card>
                    <StatusesContainer character={combat.enemy}/>
                </Card>
            </CardGroup>
            <CardGroup itemsPerRow={3}>
                    <CharacterContainer character={combat.player}/>
                <Button className="button-fixed-width" style={{ fontSize: '16px' }}>Choose A Technique</Button>
                    <CharacterContainer character={combat.enemy}/>
            </CardGroup>
            </Segment>
        );
    } else {
        return (
            <Segment>
            <RoundCard/>
            <CardGroup itemsPerRow={3}>
                <Card>
                    <StatusesContainer character={combat.player}/>
                </Card>
                <Button className="button-fixed-width"style={{ fontSize: '20px' }}>Round: {combat.rnd}
                <br/>
                <br/>{combat.enemy.name}'s Turn</Button>
                <Card>
                    <StatusesContainer character={combat.enemy}/>
                </Card>
            </CardGroup>
            <CardGroup itemsPerRow={3}>
                    <CharacterContainer character={combat.player}/>
                <Button onClick={enemyAction} className="button-fixed-width" style={{ fontSize: '16px' }}>Brace Yourself!
                <br />
                <br />
                (Click Here)
                </Button>
                    <CharacterContainer character={combat.enemy}/>
            </CardGroup>
            </Segment>
        //round number
        //CharacterContainer passing combat.player as prop 
        //StatusesContainer passing combat.player
        //CharacterContainer passing combat.enemy as prop
        //StatusesContainer passing combat.enemy
        );
    }
  }
  
  export default Combat;