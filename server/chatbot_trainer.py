from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from typing import List, Dict
from config.file_reader import read_files

BOT_NAME = "Cinebot"
DATA = ["data/greetings.json", "data/questions.json"]

class ChatbotTrainer:
    def __init__(self, name: str, files: List[str]):
        self.chatbot = ChatBot(name)
        self.trainer = ListTrainer(self.chatbot)
        self.files = files

    def train(self) -> None:
        convos = read_files(self.files)
        for convo in convos:
            questions = convo.get("questions")
            answer = convo.get("answer")
            for question in questions:
                self.trainer.train([question, answer])

if __name__ == "__main__":
    chatbot_trainer = ChatbotTrainer(BOT_NAME, DATA)
    chatbot_trainer.train()

