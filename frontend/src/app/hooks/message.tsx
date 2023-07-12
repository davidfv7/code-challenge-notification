import axios from 'axios';
import { message } from '../types/notification';

const useMessage = () => {
    const send = async (payload: message) => {
        return await axios.post("/api/messages", payload)
            .then(res => {
                if (res.data) {
                    return res.data
                }
            })
    };
    return [send] as const;
};

export default useMessage