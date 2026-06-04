import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = os.getenv("BASE_URL_SHEETY") + "/" + os.getenv("USERNAME_SHEETY") + "/" + os.getenv("PROJECT_NAME_SHEETY") + "/" + os.getenv("FIRST_SHEET_NAME_SHEETY") # get the url of the sheet

class DataManager:
    def __init__(self):
        """this class is responsible for getting the data from the sheet"""
        self._user = os.getenv("USERNAME_SHEETY") # get the username
        self._password = os.getenv("PASSWORD_SHEETY") # get the password
        self._authorization = {"Authorization": f"Bearer {os.getenv("BOT_TOKEN")}"} # get the token
        self.destination_data = {} # create an empty dictionary

    def get_destination_data(self):
        """
        get all the data in that sheet
        :return: all the data in that sheet
        """
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self._authorization) # get the data from the sheet
        data = response.json() # get the data in JSON format
        self.destination_data = data["prices"] # save the data in a dictionary
        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        """
        Update the lowest price
        :param row_id: Row ID
        :param new_price: New price
        :return: status code
        """
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}", headers=self._authorization, json=new_data)
        return response.status_code