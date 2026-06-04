import requests
import os
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    def __init__(self):
        """this class is responsible for searching for flights"""
        self._api_key = os.getenv("API_KEY_SERP_API") # get the API key

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        """
        Check flights
        :param origin_city_code: Origin city code
        :param destination_city_code: Destination city code
        :param from_time: from time
        :param to_time: to time
        :return: flight data
        """
        endpoint = os.getenv("BASE_URL_SERP_API")
        params = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "adults": "2",
            "currency": "EUR",
            "hl": "en",
            "api_key": self._api_key,
        }

        response = requests.get(url=endpoint, params=params)
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None

        data = response.json()
        if "error" in data:
            print(f"API error: {data['error']}")
            return None
        return data