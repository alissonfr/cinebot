import os
from app.trainer import ChatbotTrainer
from chatterbot import ChatBot

class ChatbotService:
    def __init__(self, bot_name: str, data_path: str):
        self.bot_name = bot_name
        self.data_path = data_path
        self.bot = self.initialize_bot()

    def initialize_bot(self):
        trainer = ChatbotTrainer(self.bot_name, self.data_path)
        trainer.train()
        return ChatBot(self.bot_name, read_only=True, logic_adapters=[{"import_path": "chatterbot.logic.BestMatch"}])

    def get_response(self, question: str):
        response = self.bot.get_response(question.lower())
        return response