export enum MessageType {
    ADMIN,
    USER
}

export interface Message {
    id: number;
    type: MessageType;
    message: string;
}

export const messages: Message[] = [
    {
        id: 1,
        type: MessageType.ADMIN,
        message: 'Ola humano',
    },
    {
        id: 2,
        type: MessageType.USER,
        message: 'Hey!',
    }
]

interface User {
    avatar: string;
    name: string;
}

export const bot: User = {
    avatar: '/cinebot.png',
    name: 'Cinebot',
};

export const user: User = {
    avatar: '/user.png',
    name: 'Voce',
};
