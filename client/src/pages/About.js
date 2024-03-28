import React from "react";
import { useNavigate } from "react-router-dom";
import HHLogo from '../images/HHLogo.png';
import BWLogo from '../images/BWLogo.png'
import { Button, Segment, Header, CardMeta,
    CardHeader,
    CardDescription,
    CardContent,
    Card,
    Icon,
    Image, CardGroup, Container} from 'semantic-ui-react'
    import MapImage from "../images/Baleweld.webp"

function About() {
  
  const navigate = useNavigate();

  function navBack(){
    navigate('/')
  }

return(
      <Segment
      style={{
        backgroundImage: `url(${MapImage})`,
        backgroundSize: 'cover', // Adjust as needed
        backgroundPosition: 'center', // Adjust as needed
        width: "auto",
        height: "1000px"
      }}>
        <Button onClick={navBack}>Home</Button>
        <br/>
        
        <Container text textAlign="left" style={{
        backgroundColor: "gray"
      }}>
            <Header as='h1' color = "olive">About Heroes' Hall: Baleweld</Header>
            <p>
                Heroes' Hall is a long running passion project of mine. 
                It is a medieval fantasy tabletop game where players command rival guilds of adventuring heroes. 
            </p>
            <p>
                This app is my first shot at programming a stripped-down version of the turn-based combat and the origin of one of the greatest threats to the world of Heroes' Hall.
            </p>
            <p>
                In this app, venture into the Baleweld, the ever-wood, the primordial forest. Hunt the weald's mystical denizens, strengthen your Hero and take on aspects of the Beasts you defeat. <br/>How far will you push your Hero to change? How long until you no longer recognize the eager adventurer that first set out? 
            </p>
            <p>
                ...And when the gristly work is done, will Light finally be brought to the Baleweld? Or will it be conquered by the most Baleful Beast of all?
            </p>
            <img src={BWLogo} alt="Baleweld Logo" style={{ width: '500px', height: 'auto'}}/>
            
        </Container>
        
      </Segment>
    )
}

export default About;

