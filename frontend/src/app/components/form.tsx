"use client";
import '../styles/form.css';
import { useState } from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import Alert from '@mui/material/Alert';
import useMessage from '../hooks/message';

import Stack from '@mui/material/Stack';

import Snackbar from '@mui/material/Snackbar';

export default function NotificationForm() {
    const categories = [
        { label: 'Sports' },
        { label: 'Finances' },
        { label: 'Movies' },

    ]
    const [showAlert, setShowAlert] = useState(false);
    const [severity, setSeverity] = useState("success");
    const [alertMesssage, setAlertMessage] = useState("");
    const [send] = useMessage();
    const [message, setMessage] = useState({
        "category": "",
        "message": ""
    });
    function handleClose() {
        setShowAlert(false)
    }
    function handleCategoryChange(event: any, newValue: any) {
        if (newValue) {
            const mess = { ...message, category: newValue["label"] }
            setMessage(mess)
        }
    }
    function handleMessageChange(event: React.ChangeEvent<HTMLInputElement>) {
        const mess = { ...message, message: event.target.value }
        setMessage(mess)
    }

    async function sendMessage() {
        if (message.message !== "" && message.category !== "") {
            const res = await send(message);
            if (res.success) {
                setSeverity("success")
                setAlertMessage("Message has been created and will be sent soon!")
                setShowAlert(true)
                setMessage({
                    "category": "",
                    "message": ""
                })
            }
        } else {
            setSeverity("error")
            setAlertMessage("You need to complete the fields first.")
            setShowAlert(true)
        }
    }
    return (
        <div className='notificationForm'>
            <Stack spacing={2} sx={{ width: '100%' }}>
                <Snackbar anchorOrigin={ {vertical: "top", horizontal:"center"} } open={showAlert} autoHideDuration={4000} onClose={handleClose}>
                    <Alert onClose={handleClose} severity={severity} sx={{ width: '100%' }}>
                        {alertMesssage}
                    </Alert>
                </Snackbar>
            </Stack>
            <h1>Write a new message</h1>
            <form >
                <Autocomplete
                    id="combo-box-demo"
                    options={categories}
                    getOptionLabel={(option) => option.label}
                    defaultValue={categories[0]}
                    sx={{ width: 300 }}
                    onChange={handleCategoryChange}
                    renderInput={(params) => <TextField key={params.id} {...params} label="Category" />}
                />
                <TextField
                    id="filled-multiline-flexible"
                    label="Message"
                    multiline
                    onChange={handleMessageChange}
                    value={message.message}
                    variant="filled"
                />
                <Button onClick={() => sendMessage()}>Send</Button>
            </form>
        </div>
    )
}
