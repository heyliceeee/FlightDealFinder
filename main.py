from data_manager import DataManager
from pprint import pprint
import requests_cache
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

requests_cache.install_cache("flight_cache", urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }) # cache the data for 1 hour

ORIGIN_CITY_IATA = "OPO" # origin city

# Sheety API
data_manager = DataManager()
sheet_data = data_manager.get_destination_data() # get data from a sheet

tomorrow = datetime.now() + timedelta(days=1) # get tomorrow's date
one_month_from_today = datetime.now() + timedelta(days=(1 * 30)) # get 1 month from today

flight_search = FlightSearch()
notification_manager = NotificationManager()


for destination in sheet_data: # loop through all the destinations
    pprint(f"Searching best price for {destination['city']}...")

    search_start = tomorrow # start searching from tomorrow
    search_end = one_month_from_today # end searching 1 month from today

    current_date = search_start # current date
    best_flight = None # best flight

    while current_date <= search_end: # loop through the dates
        direct_data = flight_search.check_flights(ORIGIN_CITY_IATA, destination["iataCode"], current_date, current_date + timedelta(days=3), is_direct=True) # search for direct flights
        #flights = flight_search.check_flights(ORIGIN_CITY_IATA, destination["iataCode"], current_date, current_date + timedelta(days=3)) # search for flights

        flight = find_cheapest_flight(direct_data) # find the cheapest direct flight

        if flight.price == "N/A": # if no there exists a direct flight
            pprint(f"No direct flight on {current_date.date()} → checking indirect flights...")
            indirect_data = flight_search.check_flights(ORIGIN_CITY_IATA, destination["iataCode"], current_date, current_date + timedelta(days=3), is_direct=False) # search for indirect flights
            flight = find_cheapest_flight(indirect_data) # find the cheapest indirect flight

        if flight.price != "N/A": # if found a flight (direct or indirect)
            if best_flight is None or flight.price < best_flight.price: # check if this flight is the best
                best_flight = flight # update the best flight

        current_date += timedelta(days=1) # move to the next date

    if best_flight is None: # check if there are no flights
        pprint(f"No flights found for {destination['city']}.")
        continue

    pprint(f"Cheapest flight to {destination['city']}: {best_flight.price}€ | {best_flight.stops} stops | {best_flight.out_date}")

    if best_flight.price < destination["lowestPrice"]: # check if the price is lower than the current lowest price
        pprint(f"Lower price found for {destination['city']}!")
        data_manager.update_lowest_price(destination["id"], best_flight.price) # update the lowest price

        text = (
            f"🔥 *Lower Price Alert!* 🔥\n"
            f"✈️ Only *{best_flight.price}€* to fly from "
            f"*{ORIGIN_CITY_IATA} → {destination['iataCode']}*\n"
            f"📅 On *{best_flight.out_date}*\n"
            f"🔁 Stops: *{best_flight.stops}*"
        )

        notification_manager.send_telegram_message(text) # send a notification to Telegram