from flask import Flask, request, jsonify
from responses import get_response

app = Flask(_name_)

@app.route('/webhook',
method=['POST'])
def telegram_webhook():
    data = request.get_json()
    # ambil chat_id dan message
    chat_id = data['message']['chat']['id']
    text = data['message']['text']

    # balasan sederhana
    reply = "Halo! Kamu bilang: " + text

    # kirim balasan via Telegram API
    requests.post(f"https://api.telegram.org/bot{7529576898:AAF6yPDIOhbhFRhHTh6Qff32bgDCXf_nGiY}/sendMessage", json={
        "chat_id": chat_id,
        "text": reply
    })
    return jsonify({"ok": True})

def home():
    return "✅ Chatbot CS is Live!"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = get_response(user_input)
    return jsonify({"response": response})

if _name_ == "_main_":
    app.run(debug=True)
