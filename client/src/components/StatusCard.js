import React, { useEffect, useState, useContext } from "react";
import { Button, Segment, Header, CardMeta,
  CardHeader,
  CardDescription,
  CardContent,
  Card,
  Icon,
  Image, CardGroup} from 'semantic-ui-react'

//shows status- effect and duration


function StatusCard({status}) {

    return(
      <CardDescription>{status['affected_stat']}: {status['amnt']}, Rnds remaining: {status['remaining_duration']}</CardDescription>
    )
  }
  
  export default StatusCard;