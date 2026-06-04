from datetime import datetime, timedelta

class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date):
        """
        this class is responsible for storing the flight data
        :param price: Price of the flight
        :param origin_airport: Origin airport
        :param destination_airport: Destination airport
        :param out_date: Outbound date
        """
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date

def find_cheapest_flight(data):
    """
    Find the cheapest flight
    :param data: Data from the API
    :return: flight data
    """
    if data is None or (not data.get("best_flights") and not data.get("other_flights")): # check if there are flights
        print("No flights found.")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A") # return None

    all_flights = data.get("best_flights", []) + data.get("other_flights", []) # get all the flights

    first_flight = all_flights[0] # get the first flight
    lowest_price = first_flight["price"] # get the lowest price
    origin = first_flight["flights"][0]["departure_airport"]["id"] # get the origin airport
    destination = first_flight["flights"][-1]["arrival_airport"]["id"] # get the destination airport
    out_date = first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0] # get the outbound date

    cheapest_flight = FlightData(lowest_price, origin, destination, out_date) # create a new FlightData object

    for flight in all_flights: # loop through all the flights
        try:
            price = flight["price"] # get the price
        except KeyError:
            print("--- No price available for flight. ---")
            continue
        if price < lowest_price: # check if the price is lower than the current lowest price
            lowest_price = price # update the lowest price
            origin = flight["flights"][0]["departure_airport"]["id"] # update the origin airport
            destination = flight["flights"][-1]["arrival_airport"]["id"] # update the destination airport
            out_date = flight["flights"][0]["departure_airport"]["time"].split(" ")[0] # update the outbound date
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date) # update the FlightData object
            print(f"Lowest price to {destination} is {lowest_price}€")

    return cheapest_flight