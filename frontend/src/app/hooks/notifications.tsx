import axios from 'axios';
import { useState } from 'react';
const useNotifications = () => {
    const [notifications, setData] = useState({records: [], total:0});

    const fetch = async (page: number, rowsPerPage: number) => {
        await axios.get(`/api/notifications?page=${page}&size=${rowsPerPage}`)
            .then(res => {
                if (res.data) {
                    setData(res.data)
                }
            })
    };


    return [notifications, fetch] as const;
};

export default useNotifications