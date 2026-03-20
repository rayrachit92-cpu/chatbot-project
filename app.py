from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Global memory
chat_history = ""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global chat_history

    user_input = request.json["message"]

    # Add user message to history
    chat_history += f"User: {user_input}\nAI: "

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": chat_history,
            "stream": False
        }
    )

    reply = response.json()["response"].strip()

    # Add AI reply to history
    chat_history += reply + "\n"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)