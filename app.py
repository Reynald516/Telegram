from flask import Flask, request, jsonify
from responses import get_response

app = Flask(_name_)

@app.route("/")
def home():
    return "✅ Chatbot CS is Live!"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = get_response(user_input)
    return jsonify({"response": response})

if _name_ == "_main_":
    app.run(debug=True)
