import axios from 'axios';
import { useState, useEffect } from 'react';

const useFetchNotifications = () => {
    const [notifications, setData] = useState([]);
    useEffect(() => {
        axios.get("/api/notifications")
            .then(res => {
                if (res.data) {
                    setData(res.data)
                }
            })
    }, []);


    return notifications;
};

export default useFetchNotifications