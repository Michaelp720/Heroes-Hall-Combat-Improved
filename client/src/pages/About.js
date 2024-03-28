import React from "react";
import { useNavigate } from "react-router-dom";
import HHLogo from '../images/HHLogo.png';
import { Button, Segment, Header, CardMeta,
    CardHeader,
    CardDescription,
    CardContent,
    Card,
    Icon,
    Image, CardGroup, Container} from 'semantic-ui-react'

function About() {
  
  const navigate = useNavigate();

  function navBack(){
    navigate('/')
  }

return(
      <Segment>
        <Button onClick={navBack}>Home</Button>
        <br/>
        
        <Container text textAlign="left">
            <Header as='h2'>About Heroes' Hall</Header>
            <p>
                Heroes' Hall is a long running passion project of mine. 
                It is a medieval fantasy tabletop game where players command rival guilds of adventuring heroes. 
            </p>
            <p>
                This app is my first shot at programming a stripped-down version of the turn-based combat.
            </p>
            <img src={HHLogo} alt="Heroes' Hall Logo" style={{ width: '700px', height: 'auto' }}/>
        </Container>
        
      </Segment>
    )
}

export default About;

