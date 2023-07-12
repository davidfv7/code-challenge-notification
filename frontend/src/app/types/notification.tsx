type notification = {
    id: number;
    user_id: number;
    category: string;
    user: {
        name: string;
        email: string;
    }
    message: {
        category: string;
        message: string;
        status: string;
        id: number;
        created_at: string;
    };
    status: string;
    created_at: string;
    send_at: string;
}

type message = {
    category: string;
    message: string;
}

export type { notification, message }