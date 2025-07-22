from flask import Flask, request, jsonify
from responses import get_response
import requests

app = Flask(_name_)  # <- ini salah sebelumnya: _name harusnya _name_

@app.route('/')
def home():
    return "✅ Chatbot CS is Live!"

@app.route('/webhook', methods=['POST'])  # <- methods, bukan method
def telegram_webhook():
    data = request.get_json()

    # Pastikan struktur JSON sesuai
    if "message" not in data:
        return jsonify({"ok": False, "error": "No message found"}), 400

    chat_id = data['message']['chat']['id']
    text = data['message'].get('text', '')

    reply = f"Halo! Kamu bilang: {text}"

    # GANTI token bot Telegram kamu yang valid
    TELEGRAM_BOT_TOKEN = "7529576898:AAF6yPDIOhbhFRhHTh6Qff32bgDCXf_nGiY"

    send_message_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    response = requests.post(send_message_url, json={
        "chat_id": chat_id,
        "text": reply
    })

    return jsonify({"ok": True, "response": response.json()})


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    response = get_response(user_input)
    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True)
