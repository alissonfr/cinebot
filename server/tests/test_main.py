
from os import path
from flask import Flask
import sys
import unittest
from unittest import TestCase

ROOT_FOLDER = path.abspath(path.join(path.dirname(__file__), '..'))
sys.path.append(ROOT_FOLDER)

from app.main import Main
from app.services.chatbot_service import ChatbotService
from app.config.constants import MINIMAL_CONFIDENCE, BOT_NAME, DATA_PATH

GREETINS = [
    ("oi", "Oi! Como posso ajudar?"),
    ("olá", "Oi! Como posso ajudar?"),
    ("e aí", "Oi! Como posso ajudar?"),
    ("opa", "Oi! Como posso ajudar?"),
    ("oi, tudo bem?", "Oi! Como posso ajudar?"),
    ("oii", "Oi! Como posso ajudar?"),
    ("oieh", "Oi! Como posso ajudar?"),
    ("bom dia", "Bom dia! Espero que seu dia seja ótimo!"),
    ("bom dia, como vai?", "Bom dia! Espero que seu dia seja ótimo!"),
    ("bom dia, tudo bem?", "Bom dia! Espero que seu dia seja ótimo!"),
    ("um bom dia para você", "Bom dia! Espero que seu dia seja ótimo!"),
    ("boa tarde", "Boa tarde! Como posso ajudar você?"),
    ("boa tarde, tudo bem?", "Boa tarde! Como posso ajudar você?"),
    ("boa tarde, como você está?", "Boa tarde! Como posso ajudar você?"),
    ("uma boa tarde para você", "Boa tarde! Como posso ajudar você?"),
    ("boa noite", "Boa noite! Espero que tenha um bom descanso."),
    ("boa noite, tudo bem?", "Boa noite! Espero que tenha um bom descanso."),
    ("boa noite, como vai?", "Boa noite! Espero que tenha um bom descanso."),
    ("tenha uma boa noite", "Boa noite! Espero que tenha um bom descanso.")
]
BASIC_INFO = [
    ("o que você faz?", "Eu sou um assistente virtual e posso ajudar com uma variedade de tarefas, como responder perguntas, fornecer informações, ajudar com problemas técnicos e muito mais. Como posso ajudar você hoje?"),
    ("quais são suas funções?", "Eu sou um assistente virtual e posso ajudar com uma variedade de tarefas, como responder perguntas, fornecer informações, ajudar com problemas técnicos e muito mais. Como posso ajudar você hoje?"),
    ("o que você pode fazer?", "Eu sou um assistente virtual e posso ajudar com uma variedade de tarefas, como responder perguntas, fornecer informações, ajudar com problemas técnicos e muito mais. Como posso ajudar você hoje?"),
    ("como você pode me ajudar?", "Eu sou um assistente virtual e posso ajudar com uma variedade de tarefas, como responder perguntas, fornecer informações, ajudar com problemas técnicos e muito mais. Como posso ajudar você hoje?"),
    ("como interagir com você?", "Você pode interagir comigo simplesmente fazendo perguntas ou pedindo ajuda sobre qualquer assunto. Basta digitar o que você precisa saber ou o que deseja fazer, e eu farei o meu melhor para ajudar."),
    ("como posso falar com você?", "Você pode interagir comigo simplesmente fazendo perguntas ou pedindo ajuda sobre qualquer assunto. Basta digitar o que você precisa saber ou o que deseja fazer, e eu farei o meu melhor para ajudar."),
    ("qual é a melhor maneira de usar seus serviços?", "Você pode interagir comigo simplesmente fazendo perguntas ou pedindo ajuda sobre qualquer assunto. Basta digitar o que você precisa saber ou o que deseja fazer, e eu farei o meu melhor para ajudar."),
    ("como eu posso fazer perguntas para você?", "Você pode interagir comigo simplesmente fazendo perguntas ou pedindo ajuda sobre qualquer assunto. Basta digitar o que você precisa saber ou o que deseja fazer, e eu farei o meu melhor para ajudar."),
    ("quais perguntas você responde?", "Eu posso responder a uma ampla gama de perguntas sobre diversos tópicos, como informações gerais, ajuda técnica, curiosidades e muito mais. Se tiver uma pergunta específica, sinta-se à vontade para perguntar!"),
    ("o que você pode responder?", "Eu posso responder a uma ampla gama de perguntas sobre diversos tópicos, como informações gerais, ajuda técnica, curiosidades e muito mais. Se tiver uma pergunta específica, sinta-se à vontade para perguntar!"),
    ("que tipo de perguntas você pode responder?", "Eu posso responder a uma ampla gama de perguntas sobre diversos tópicos, como informações gerais, ajuda técnica, curiosidades e muito mais. Se tiver uma pergunta específica, sinta-se à vontade para perguntar!"),
    ("quais são os tópicos que você cobre?", "Eu posso responder a uma ampla gama de perguntas sobre diversos tópicos, como informações gerais, ajuda técnica, curiosidades e muito mais. Se tiver uma pergunta específica, sinta-se à vontade para perguntar!"),
    ("o que você não pode fazer?", "Embora eu possa ajudar com muitas coisas, há algumas limitações. Por exemplo, eu não posso fornecer conselhos médicos específicos, realizar transações financeiras ou acessar informações pessoais. Se você tiver dúvidas sobre algo fora do meu alcance, tentarei orientá-lo da melhor forma possível."),
    ("quais são as suas limitações?", "Embora eu possa ajudar com muitas coisas, há algumas limitações. Por exemplo, eu não posso fornecer conselhos médicos específicos, realizar transações financeiras ou acessar informações pessoais. Se você tiver dúvidas sobre algo fora do meu alcance, tentarei orientá-lo da melhor forma possível."),
    ("há algo que você não consegue fazer?", "Embora eu possa ajudar com muitas coisas, há algumas limitações. Por exemplo, eu não posso fornecer conselhos médicos específicos, realizar transações financeiras ou acessar informações pessoais. Se você tiver dúvidas sobre algo fora do meu alcance, tentarei orientá-lo da melhor forma possível."),
    ("o que você não é capaz de responder?", "Embora eu possa ajudar com muitas coisas, há algumas limitações. Por exemplo, eu não posso fornecer conselhos médicos específicos, realizar transações financeiras ou acessar informações pessoais. Se você tiver dúvidas sobre algo fora do meu alcance, tentarei orientá-lo da melhor forma possível.")
]

MAIN_QUESTIONS = [
    ("quem dirigiu o filme o poderoso chefão?", "O filme 'O Poderoso Chefão' foi dirigido por Francis Ford Coppola."),
    ("quem é o diretor de o poderoso chefão?", "O filme 'O Poderoso Chefão' foi dirigido por Francis Ford Coppola."),
    ("qual é o nome do diretor do poderoso chefão?", "O filme 'O Poderoso Chefão' foi dirigido por Francis Ford Coppola."),
    ("quem foi responsável pela direção de o poderoso chefão?", "O filme 'O Poderoso Chefão' foi dirigido por Francis Ford Coppola."),
    ("em que ano foi lançado pulp fiction?", "O filme 'Pulp Fiction' foi lançado em 1994."),
    ("qual é o ano de lançamento de pulp fiction?", "O filme 'Pulp Fiction' foi lançado em 1994."),
    ("quando pulp fiction foi lançado?", "O filme 'Pulp Fiction' foi lançado em 1994."),
    ("em que ano pulp fiction chegou aos cinemas?", "O filme 'Pulp Fiction' foi lançado em 1994."),
    ("quem interpretou tony montana no filme scarface?", "Tony Montana foi interpretado por Al Pacino no filme 'Scarface'."),
    ("quem é o ator de tony montana em scarface?", "Tony Montana foi interpretado por Al Pacino no filme 'Scarface'."),
    ("qual ator faz tony montana em scarface?", "Tony Montana foi interpretado por Al Pacino no filme 'Scarface'."),
    ("quem vive tony montana em scarface?", "Tony Montana foi interpretado por Al Pacino no filme 'Scarface'."),
    ("qual é o nome do personagem principal em taxi driver?", "O personagem principal em 'Taxi Driver' é Travis Bickle."),
    ("quem é o protagonista de taxi driver?", "O personagem principal em 'Taxi Driver' é Travis Bickle."),
    ("como se chama o personagem principal de taxi driver?", "O personagem principal em 'Taxi Driver' é Travis Bickle."),
    ("quem é o personagem central em taxi driver?", "O personagem principal em 'Taxi Driver' é Travis Bickle."),
    ("qual é o nome do personagem interpretado por uma thurman em kill bill?", "Uma Thurman interpreta Beatrix Kiddo, também conhecida como A Noiva, em 'Kill Bill'."),
    ("quem uma thurman interpreta em kill bill?", "Uma Thurman interpreta Beatrix Kiddo, também conhecida como A Noiva, em 'Kill Bill'."),
    ("como se chama a personagem de uma thurman em kill bill?", "Uma Thurman interpreta Beatrix Kiddo, também conhecida como A Noiva, em 'Kill Bill'."),
    ("qual é o nome da personagem de uma thurman em kill bill?", "Uma Thurman interpreta Beatrix Kiddo, também conhecida como A Noiva, em 'Kill Bill'.")
]

class TestBase(TestCase):
    def setUp(self):
        self.bot_service = ChatbotService(BOT_NAME, DATA_PATH)

    def get_response(self, message, expected_answer):
        answer = self.bot_service.get_response(message)
        self.assertGreater(answer.confidence, MINIMAL_CONFIDENCE)
        self.assertIn(expected_answer, answer.text)

class TestMain(TestBase):
    def setUp(self):
        self.app = Main().app
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app_creation(self):
        self.assertIsNotNone(self.app)
        self.assertIsInstance(self.app, Flask)

class TestTrainer(TestBase):
    def test_greetings(self):
        convos = GREETINS
        for question, answer in convos:
            with self.subTest(mensagem=question):
                self.get_response(question, answer)

    def test_basic_info(self):
        convos = BASIC_INFO
        for question, answer in convos:
            with self.subTest(mensagem=question):
                self.get_response(question, answer)

    def test_main_questions(self):
        convos = MAIN_QUESTIONS
        for question, answer in convos:
            with self.subTest(mensagem=question):
                self.get_response(question, answer)

if __name__ == '__main__':
    unittest.main()