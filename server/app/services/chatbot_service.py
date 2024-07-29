import os
from trainer import ChatbotTrainer
from chatterbot import ChatBot
from config.constants import DB_NAME

class ChatbotService:
    def __init__(self, bot_name: str, data_path: str):
        self.bot_name = bot_name
        self.data_path = data_path
        self.bot = self.initialize_bot()

    def initialize_bot(self):
        if not os.path.exists(DB_NAME):
            trainer = ChatbotTrainer(self.bot_name, self.data_path)
            trainer.train()
        return ChatBot(self.bot_name, read_only=True, logic_adapters=[{"import_path": "chatterbot.logic.BestMatch"}])

    def get_response(self, question: str):
        response = self.bot.get_response(question.lower())
        return response