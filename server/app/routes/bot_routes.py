from flask import Blueprint, request, jsonify
from config.constants import MINIMAL_CONFIDENCE
from services.chatbot_service import ChatbotService
from config.constants import MINIMAL_CONFIDENCE, BOT_NAME, DATA_PATH

bot_blueprint = Blueprint('bot', __name__)
bot_service = ChatbotService(BOT_NAME, DATA_PATH)

@bot_blueprint.get("/question")
def get_answer():
    question = request.args.get('question', '')
    if not question:
        return jsonify(
            answer="Pergunta não fornecida.",
            confidence=0
        )
    response = bot_service.get_response(question)
    if response.confidence >= MINIMAL_CONFIDENCE:
        return jsonify(
            answer=response.text,
            confidence=response.confidence
        )
    else:
        return jsonify(
            answer="Ainda não sei responder essa pergunta :(",
            confidence=response.confidence
        )
