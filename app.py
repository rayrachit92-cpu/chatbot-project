from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Global memory
chat_history = ""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global chat_history

    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"reply": "No message received"}), 400

    user_input = data["message"]

    # Add user message to history
    chat_history += f"User: {user_input}\nAI: "

    # 🔥 TEMP FIX (since Ollama not available on Render)
    reply = f"You said: {user_input}"

    # Add AI reply to history
    chat_history += reply + "\n"

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run()
