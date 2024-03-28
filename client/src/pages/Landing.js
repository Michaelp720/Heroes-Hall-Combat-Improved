//checks session, login, logout

import React, { useEffect, useState, useContext } from "react";
import {PlayerContext} from '../context/player'
import { Button, Segment, Header } from 'semantic-ui-react'
import { useNavigate } from "react-router-dom";
import '../index.css'
import HHLogo from '../images/HHLogo.png';
import BWLogo from '../images/BWLogo.png'
import MapImage from "../images/Baleweld.webp"

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
      <Segment style={{
        backgroundImage: `url(${MapImage})`,
        backgroundSize: 'cover', // Adjust as needed
        backgroundPosition: 'center', // Adjust as needed
        width: "auto",
        height: "1000px"
      }}>
        
        <Button onClick={handleLogout}>Logout</Button>
        
        <Header as = 'h1' color = "olive">Welcome, {player.name}, to...</Header>
        <img src={HHLogo} alt="Heroes' Hall Logo" style={{ width: '700px', height: 'auto' }} onClick = {navAbout}/>
        <br/>
        <img src={BWLogo} alt="Baleweld Logo" style={{ width: '550px', height: 'auto'}} onClick = {navAbout}/>
        <br/>
        <Button onClick={navAdvancement}>Advance Character</Button>
        <Button onClick={navVenture}>Venture into the Baleweld...</Button>
      </Segment>
    )
  } 
  else {
    return (
      <Segment style={{
        backgroundImage: `url(${MapImage})`,
        backgroundSize: 'cover', // Adjust as needed
        backgroundPosition: 'center', // Adjust as needed
        width: "auto",
        height: "1000px"
      }}>
        <Button onClick={navLogin}>Login to Begin your Journey!</Button>
        <br/>
        <img src={HHLogo} alt="Heroes' Hall Logo" style={{ width: '900px', height: 'auto' }}/>
        <br/>
        <img src={BWLogo} alt="Baleweld Logo" style={{ width: '500px', height: 'auto'}}/>
      </Segment>
    )
  }
  
}

export default Landing;

//        <header className="title-card">Heroes' Hall: Combat</header>