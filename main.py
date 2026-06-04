from data_manager import DataManager
from pprint import pprint
import requests_cache
from datetime import datetime, timedelta
from flight_search import FlightSearch

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

# Sheety API
data_manager = DataManager()
sheet_data = data_manager.get_destination_data() # get data from a sheet
#pprint(sheet_data) # pretty print

tomorrow = datetime.now() + timedelta(days=1) # get tomorrow's date
six_months_from_today = datetime.now() + timedelta(days=180) # get 6 months from today

# Flight Search
flight_search = FlightSearch()
flights = flight_search.check_flights("OPO", "CDG", tomorrow, six_months_from_today)
pprint(flights)