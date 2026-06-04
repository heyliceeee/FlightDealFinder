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

ORIGIN_CITY_IATA = "OPO" # origin city

# Sheety API
data_manager = DataManager()
sheet_data = data_manager.get_destination_data() # get data from a sheet

tomorrow = datetime.now() + timedelta(days=1) # get tomorrow's date
six_months_from_today = datetime.now() + timedelta(days=(6 * 30)) # get 6 months from today

flight_search = FlightSearch()

# Search all the cities
for destination in sheet_data: # loop through all the cities
    pprint(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(ORIGIN_CITY_IATA, destination["iataCode"], tomorrow, six_months_from_today) # get flights for the city

    cheapest_flight = find_cheapest_flight(flights, six_months_from_today.strftime("%Y-%m-%d")) # get the cheapest flight
    pprint(f"{destination['city']}: {cheapest_flight.price}€")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]: # check if the price is lower than the lowest price in the sheet
        pprint(f"Lower price flight found to {destination['city']}!")
        data_manager.update_lowest_price(destination["id"], cheapest_flight.price) # update the lowest price in the sheet