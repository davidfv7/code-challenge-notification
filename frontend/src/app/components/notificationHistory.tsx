'use client';

import '../styles/logs.css'
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';
import Button from '@mui/material/Button';
import { useEffect } from 'react';
import useNotifications from '../hooks/notifications';
import {useState} from 'react';


export default function NotificationHistory() {
  const [notifications , fetch] = useNotifications();
  const [page, setPage] = useState(0)
  const [rowsPerPage, setRowsPerPage] = useState(5)
  interface Column {
    label: string
  }
  function handleChangeRowsPerPage(event: any){
    setRowsPerPage(event.target.value);
    setPage(0);
  }

  function handleChangePage(event: unknown, newPage: number){
    setPage(newPage);
  }

  const columns: readonly Column[] = [
    { label: 'User Email' },
    { label: 'User Name' },
    { label: 'Category'},
    { label: 'Message'},
    { label: 'Status'},
    { label: 'Type'},
    { label: 'Send At'},
  ]
  useEffect(() => {
    fetch(page + 1, rowsPerPage);
  }, [page, rowsPerPage])
  return (
    <div className='logContainer'>
      <h1>Notification History</h1>
      <Button onClick={() => fetch(page + 1, rowsPerPage)}>Refresh</Button>
      <Paper sx={{ width: '100%', overflow: 'hidden' }}>
      <TableContainer sx={{ maxHeight: 440 }}>
        <Table stickyHeader aria-label="sticky table">
          <TableHead>
            <TableRow>
              {columns.map((column) => (
                <TableCell
                  key={column.label}
                >
                  {column.label}
                </TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {notifications.records.map((row) => {
                return (
                  <TableRow hover role="checkbox" tabIndex={-1} key={row.code}>
                    <TableCell >
                      {row["user"].email}
                    </TableCell>
                    <TableCell >
                      {row["user"].name}
                    </TableCell>
                    <TableCell >
                      {row["message"].category}
                    </TableCell>
                    
                    <TableCell >
                      {row["message"].message}
                    </TableCell>
                    <TableCell >
                      {row["message"].status}
                    </TableCell>
                    <TableCell >
                      {row["type"]}
                    </TableCell>
                    <TableCell >
                      {row["send_at"]}
                    </TableCell>
                  </TableRow>
                );
              })}
          </TableBody>
        </Table>
      </TableContainer>
      <TablePagination
        rowsPerPageOptions={[5, 10, 15]}
        component="div"
        count={notifications.total}
        rowsPerPage={rowsPerPage}
        page={page}
        onPageChange={handleChangePage}
        onRowsPerPageChange={handleChangeRowsPerPage}
      />
    </Paper>
      
    </div>
  )
}