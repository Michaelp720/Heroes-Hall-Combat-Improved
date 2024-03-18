import React, { useEffect, useState, useContext } from "react";
import { Button, Segment, Header } from 'semantic-ui-react'

//shows status- effect and duration


function StatusCard({status}) {

    return(
    <Segment>
      <Header as = 'h5'>{status['affected_stat']}: {status['amnt']}, Rnds remaining: {status['remaining_duration']}</Header>
    </Segment>
    )
  }
  
  export default StatusCard;