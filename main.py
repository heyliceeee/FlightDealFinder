from data_manager import DataManager
from pprint import pprint
import requests_cache
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import find_cheapest_flight

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
) # cache the data for 1 hour

# Sheety API
data_manager = DataManager()
sheet_data = data_manager.get_destination_data() # get data from a sheet
#pprint(sheet_data) # pretty print

tomorrow = datetime.now() + timedelta(days=1) # get tomorrow's date
six_months_from_today = datetime.now() + timedelta(days=(6 * 30)) # get 6 months from today

# Flight Search
flight_search = FlightSearch()
flights = flight_search.check_flights("OPO", "CDG", tomorrow, six_months_from_today)
#pprint(flights)

# Show the cheapest flight
cheapest_flight = find_cheapest_flight(flights, six_months_from_today.strftime("%Y-%m-%d")) # get the cheapest flight
pprint(f"{sheet_data[0]['city']}: {cheapest_flight.price}€")

if cheapest_flight.price != "N/A" and cheapest_flight.price < sheet_data[0]["lowestPrice"]: # check if the price is lower than the lowest price
    pprint(f"Lower price flight found to {sheet_data[0]['city']}!")
    data_manager.update_lowest_price(sheet_data[0]["id"], cheapest_flight.price) # update the lowest price in the sheet