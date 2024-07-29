import { Message, MessageType } from "@/app/data";
import ChatTopbar from "./chat-topbar";
import { ChatList } from "./chat-list";
import React, { useState } from "react";
import { sendMessage } from "@/lib/api";

interface ChatProps {
  isMobile: boolean;
}

export function Chat({ isMobile }: ChatProps) {
  const [messages, setMessages] = useState<Message[]>([]);
  const [precision, setPrecision] = useState<number>(0);


  const handleSendMessage = async (message: Message) => {
    setMessages(prevMessages => [...prevMessages, message]);
    const answer = await sendMessage(message.message);
    setPrecision(answer.confidence)
    const newMessage: Message = {
      type: MessageType.ADMIN,
      message: answer.answer
    }
    setMessages(prevMessages => [...prevMessages, newMessage]);
  }

  return (
    <div className="flex flex-col justify-between w-full h-full">
      <ChatTopbar precision={precision} />
      <ChatList
        sendMessage={handleSendMessage}
        messages={messages}
        isMobile={isMobile}
      />
    </div>
  );
}
