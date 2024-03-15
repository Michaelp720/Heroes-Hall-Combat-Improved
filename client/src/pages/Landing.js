//checks session, login, logout

import React, { useEffect, useState, useContext } from "react";
import {PlayerContext} from '../context/player'

function Landing() {
  const { player, setPlayer } = useContext(PlayerContext)

  useEffect(() => {
    fetch("/check_session").then((response) => {
      if (response.ok) {
        response.json().then((player) => setPlayer(player));
      }
    });
  }, []);

  function handleLogout(){
    fetch("/logout", {
      method: "DELETE",
    })
  }

  if (player) {
    return(
      <div>
        <h2>Welcome, {player.name}!</h2>
        <button onClick={handleLogout}>Logout</button>
        </div>
    )
  } 
  else {
    return <h2>Link to Login</h2>;
  }
  
}

export default Landing;