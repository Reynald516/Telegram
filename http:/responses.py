import json

with open("data/faqs.json", "r", encoding="utf-8") as f:
    faqs = json.load(f)

def get_response(message):
    message = message.lower()
    for faq in faqs:
        if faq["question"].lower() in message:
            return faq["answer"]
    return "Maaf, saya tidak mengerti pertanyaan Anda. Silakan hubungi CS langsung."
