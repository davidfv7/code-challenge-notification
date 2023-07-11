'use client';

import '../styles/logs.css'
import Timeline from '@mui/lab/Timeline';
import TimelineItem from '@mui/lab/TimelineItem';
import TimelineSeparator from '@mui/lab/TimelineSeparator';
import TimelineConnector from '@mui/lab/TimelineConnector';
import TimelineContent from '@mui/lab/TimelineContent';
import TimelineDot from '@mui/lab/TimelineDot';

import useFetchNotifications from '../hooks/notifications';

function getLogItems(logs) {
  return logs.map((item) => {
    return (
      <TimelineItem key={item.id}>
        <TimelineSeparator>
          <TimelineDot />
          <TimelineConnector />
        </TimelineSeparator>
        <TimelineContent>{`Notification status: ${item.status} - ${item.message} `}</TimelineContent>
      </TimelineItem>
    )
  })
}

export default function LogHistory() {
  const data = useFetchNotifications();
  return (
    <div className='logContainer'>
      <h1>Log History</h1>
      
      <Timeline>
        {getLogItems(data)}
      </Timeline>
    </div>
  )
}