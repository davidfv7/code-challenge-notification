"use client";
import  '../styles/form.css';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';

export default function NotificationForm() {
    const categories = [
        { label: 'Sports'},
        { label: 'Finances'},
        { label: 'Movies'},

    ]
    return (
        <div className='notificationForm'>
            <h1>Write a new message</h1>
        <form >
            <Autocomplete
                disablePortal
                id="combo-box-demo"
                options={categories}
                sx={{ width: 300 }}
                renderInput={(params) => <TextField {...params} label="Category" />}
            />
            <TextField
                id="filled-multiline-flexible"
                label="Message"
                multiline
                variant="filled"
            />
            <Button>Send</Button>
        </form>
        </div>
    )
}
