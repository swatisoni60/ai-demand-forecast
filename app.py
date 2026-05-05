from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)


@app.route("/api/chat/", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        message = data.get("message", "")
        model = data.get("model", "phi3")

        response = ollama.chat(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        reply = response["message"]["content"]

        return jsonify({
            "reply": reply
        })

    except Exception as e:
        return jsonify({
            "reply": f"Server error: {str(e)}"
        })


if __name__ == "__main__":
    app.run(debug=True)