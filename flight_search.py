import requests
import os
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    def __init__(self):
        """this class is responsible for searching for flights"""
        self._api_key = os.getenv("API_KEY_SERP_API") # get the API key

    def check_flights(self, origin_city_code, destination_city_code, from_time):
        """
        Check flights
        :param origin_city_code: Origin city code
        :param destination_city_code: Destination city code
        :param from_time: from time
        :return: flight data
        """
        endpoint = os.getenv("BASE_URL_SERP_API") # get the url of the API
        params = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "adults": "2",
            "currency": "EUR",
            "type": "2",
            "hl": "en",
            "api_key": self._api_key,
        } # get the parameters

        response = requests.get(url=endpoint, params=params) # get the data from the API
        if response.status_code != 200: # check if the response is OK
            print(f"check_flights() response code: {response.status_code}")
            return None

        data = response.json() # get the data in JSON format
        if "error" in data: # check if there is an error
            print(f"API error: {data['error']}")
            return None
        return data