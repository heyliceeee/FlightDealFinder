import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv
import requests

load_dotenv()

class NotificationManager:
    def __init__(self):
        """this class is responsible for sending notifications"""
        self.bot_token = os.getenv("BOT_TOKEN")
        self.chat_id = os.getenv("CHAT_ID")
        self.smtp_host = os.getenv("SMTP_HOST")
        self.smtp_port = os.getenv("SMTP_PORT")
        self.smtp_email = os.getenv("SMTP_EMAIL")
        self.smtp_pass = os.getenv("SMTP_PASSWORD")

    def send_telegram_message(self, text):
        """
        Send a Telegram message
        """
        if not text:  # if the text is empty
            return

        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        payload = {"chat_id": self.chat_id, "text": text, "parse_mode": "Markdown"}  # create the payload
        requests.post(url, data=payload)
    def send_email(self, email_list, message):
        for email in email_list:
            msg = EmailMessage()
            msg["Subject"] = "Lower Price Alert!"
            msg["From"] = self.smtp_email
            msg["To"] = email
            msg.set_content(message, charset="utf-8")

            with smtplib.SMTP(self.smtp_host, int(self.smtp_port)) as conn:  # Create an SMTP connection
                conn.starttls()  # Enable TLS encryption
                conn.login(user=self.smtp_email, password=self.smtp_pass)  # Log in to the SMTP server
                conn.send_message(msg)  # Send the email