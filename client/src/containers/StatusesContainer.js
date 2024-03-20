import React, { useEffect, useState, useContext } from "react";
import StatusCard from "../components/StatusCard"
import { Button, Segment, Header, CardMeta,
  CardHeader,
  CardDescription,
  CardContent,
  Card,
  Icon,
  Image, CardGroup} from 'semantic-ui-react'

//contains StatusCards associated with character
//fetches character's statuses


//Fetches

//State- combat, character

function StatusesContainer({character}) {

    //fetch all statuses belonging to character

    const [ statuses, setStatuses ] = useState([])
    
    
    useEffect(() => {
        fetch(`/statuses/${character['id']}`)
            .then(response => response.json())
            .then(data => setStatuses(data))
      }, [character])

    return(
    <CardContent>
      <CardHeader as ='h4'>Statuses</CardHeader>
      {statuses.map((status) => (
        <StatusCard key = {status['id']} status = {status}/>
      ))}
    </CardContent>
    )
  }
  
  export default StatusesContainer;