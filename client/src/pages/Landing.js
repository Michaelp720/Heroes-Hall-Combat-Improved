//checks session, login, logout

import React, { useEffect, useState, useContext } from "react";
import {PlayerContext} from '../context/player'
import { Button, Segment, Header } from 'semantic-ui-react'
import { useNavigate } from "react-router-dom";
import '../index.css'
import HHLogo from '../images/HHLogo.png';

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

  function navAbout(){
    navigate('/about')
  }

  if (player) {
    return(
      <Segment>
        <Button onClick={handleLogout}>Logout</Button>
        
        <Header as = 'h1'>Welcome, {player.name}, to...</Header>
        <img src={HHLogo} alt="Heroes' Hall Logo" style={{ width: '1000px', height: 'auto' }} onClick = {navAbout}/>
        <br/>
        <Button onClick={navAdvancement}>Advance Character</Button>
        <Button onClick={navVenture}>Adventure!</Button>
      </Segment>
    )
  } 
  else {
    return (
      <Segment>
        <Button onClick={navLogin}>Login to Begin your Journey!</Button>
        <br/>
        <img src={HHLogo} alt="Heroes' Hall Logo" style={{ width: '1000px', height: 'auto' }}/>
      </Segment>
    )
  }
  
}

export default Landing;

//        <header className="title-card">Heroes' Hall: Combat</header>