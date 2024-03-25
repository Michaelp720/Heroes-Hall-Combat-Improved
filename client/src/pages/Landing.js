//checks session, login, logout

import React, { useEffect, useState, useContext } from "react";
import {PlayerContext} from '../context/player'
import { Button, Segment, Header } from 'semantic-ui-react'
import { useNavigate } from "react-router-dom";

function Landing() {
  const { player, setPlayer } = useContext(PlayerContext)
  const navigate = useNavigate();

  useEffect(() => {
    fetch("/check_session").then((response) => {
      if (response.ok) {
        response.json().then((player) => setPlayer(player));
      }
    });
  }, []);

  function handleLogout() {
    fetch("/logout", {
      method: "DELETE",
    }).then(() => {
      setPlayer(null);
    });
  }

  function navLogin(){
    navigate('/login')
  }

  function navAdvancement(){
    navigate('/advancement')
  }

  function navVenture(){
    navigate('/ventures')
  }

  if (player) {
    return(
      <Segment>
        <Header>Welcome, {player.name}!</Header>
        <Button onClick={handleLogout}>Logout</Button>
        <Button onClick={navAdvancement}>Advance Character</Button>
        <br/>
        <br/>
        <Button onClick={navVenture}>Start Adventure!</Button>
      </Segment>
    )
  } 
  else {
    return (
      <Segment>
        <Button onClick={navLogin}>Login</Button>
      </Segment>
    )
  }
  
}

export default Landing;