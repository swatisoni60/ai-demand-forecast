from flask import Flask, request, jsonify
from flask_cors import CORS

# Safe import for Ollama (important for deployment)
try:
    import ollama
    OLLAMA_AVAILABLE = True
except:
    OLLAMA_AVAILABLE = False

app = Flask(__name__)
CORS(app)


# AI response function (Hybrid)
def get_ai_response(message, model="phi3"):
    if OLLAMA_AVAILABLE:
        try:
            response = ollama.chat(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            )
            return response["message"]["content"]
        except Exception as e:
            return f"Ollama error: {str(e)}"
    else:
        return "⚠️ AI works only in local mode (Ollama not available on server)."


@app.route("/api/chat/", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        message = data.get("message", "")
        model = data.get("model", "phi3")

        reply = get_ai_response(message, model)

        return jsonify({
            "reply": reply
        })

    except Exception as e:
        return jsonify({
            "reply": f"Server error: {str(e)}"
        })


@app.route("/")
def home():
    return "AI Demand Forecasting API is running 🚀"


if __name__ == "__main__":
    app.run(debug=True)
