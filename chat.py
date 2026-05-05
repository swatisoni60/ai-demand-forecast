from flask import Blueprint, request, jsonify
from utils.helpers import ask_ai

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/", methods=["POST"])
def chat():
    data = request.get_json()

    message = data["message"]

    reply = ask_ai(message)

    return jsonify({
        "reply": reply
    })