export enum MessageType {
    ADMIN,
    USER
}

export interface Message {
    type: MessageType;
    message: string;
}

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
    name: 'Você',
};
