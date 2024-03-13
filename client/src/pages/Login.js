//create a new character!

import React, { useEffect, useState, useContext } from "react";
import {PlayerContext} from '../context/player'
import { Switch, Route } from "react-router-dom";

function Login() {
  const [name, setPlayername] = useState("");
  const { player, setPlayer } = useContext(PlayerContext)

  function handleSubmit(e) {
    e.preventDefault();
    fetch("/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name }),
    }).then((r) => {
      if (r.ok) {
        r.json().then((player) => setPlayer(player));
      }
    });
    console.log(player.name)
  }

  return (
    <form onSubmit={handleSubmit}>
      <h3>Login With your Character's Name</h3>
      <label htmlFor="username">Character name: </label>
      <input
        type="text"
        id="username"
        value={name}
        onChange={(e) => setPlayername(e.target.value)}
      />
      <button type="submit">Login</button>
    </form>
  );
}

export default Login;
