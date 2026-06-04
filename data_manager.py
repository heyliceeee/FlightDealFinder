import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv("BASE_URL_SHEETY") + "/" + os.getenv("USERNAME_SHEETY") + "/" + os.getenv("PROJECT_NAME_SHEETY") + "/" + os.getenv("FIRST_SHEET_NAME_SHEETY")

class DataManager:
    def __init__(self):
        self._user = os.getenv("USERNAME_SHEETY")
        self._password = os.getenv("PASSWORD_SHEETY")
        self._authorization = {"Authorization": f"Bearer {os.getenv("BOT_TOKEN")}"}
        self.destination_data = {}

    def get_destination_data(self):
        """
        get all the data in that sheet
        :return: all the data in that sheet
        """
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self._authorization)
        data = response.json()
        self.destination_data = data["prices"] # save the data in a dictionary
        return self.destination_data