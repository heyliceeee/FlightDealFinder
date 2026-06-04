import os
from dotenv import load_dotenv
import requests

load_dotenv()

class NotificationManager:
    def __init__(self):
        """this class is responsible for sending notifications"""
        self.bot_token = os.getenv("BOT_TOKEN")
        self.chat_id = os.getenv("CHAT_ID")

    def send_telegram_message(self, text):
        """
        Send a Telegram message
        """
        if not text:  # if the text is empty
            return

        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        payload = {"chat_id": self.chat_id, "text": text, "parse_mode": "Markdown"}  # create the payload
        requests.post(url, data=payload)