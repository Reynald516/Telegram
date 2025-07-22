from flask import Flask, request
import requests
import json

app = Flask(_name_)

TELEGRAM_TOKEN = "123456789:ABCdefGhIJKlmNOPqrsTUvWxYZ"
TELEGRAM_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

@app.route('/')
def index():
    return 'Bot is running!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    chat_id = data['message']['chat']['id']
    message = data['message']['text']

    # Contoh response sederhana
    reply = f"Hi, kamu bilang: {message}"

    requests.post(TELEGRAM_URL, json={
        'chat_id': chat_id,
        'text': reply
    })

    return 'ok'

if _name_ == '_main_':
    app.run()
