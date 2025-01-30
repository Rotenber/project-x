from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Настройка CORS для разрешения запросов с любого источника

@app.route('/')
def home():
    return "Приложение работает! 🎉"

@app.route('/collect', methods=['POST'])
def collect():
    try:
        data = request.json
        print("Полученные данные:", data)

        # Отправка данных в Telegram
        send_to_telegram(data)

        return jsonify({"status": "success", "message": "Данные получены"}), 200
    except Exception as e:
        print("Ошибка:", str(e))
        return jsonify({"status": "error", "message": str(e)}), 500

def send_to_telegram(data):
    TOKEN = "7108122218:AAHg-lIHovYOKWe6BXFg5IYxf4ZX4fA8v8Y"
    CHAT_ID = "701751813"
    message = (
        f"🕵️ Данные от клиента:\n"
        f"🌐 User Agent: {data.get('userAgent')}\n"
        f"💻 Платформа: {data.get('platform')}\n"
        f"🗣 Язык: {data.get('language')}\n"
        f"📏 Экран: {data.get('screenWidth')}x{data.get('screenHeight')}\n"
        f"⏰ Временная зона: {data.get('timezone')}"
    )
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    response = requests.post(url, json={"chat_id": CHAT_ID, "text": message})
    print("Ответ Telegram:", response.json())

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

