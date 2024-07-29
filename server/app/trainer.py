from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from typing import List
import sys
from os import path

ROOT_FOLDER = path.abspath(path.join(path.dirname(__file__), '..'))
sys.path.append(ROOT_FOLDER)

from app.config.file_reader import read_files
from app.config.constants import BOT_NAME, DATA_PATH

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
    chatbot_trainer = ChatbotTrainer(BOT_NAME, DATA_PATH)
    chatbot_trainer.train()

