#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import time
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

load_dotenv()

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
TOKEN = os.getenv('TOKEN')
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ORIGIN_CITY_IATA = "LON"
# headers = {
#     "Authorization": TOKEN,
# }


data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.data["prices"]
pprint(sheet_data)
print("\n")
for data in sheet_data:
    if data["iataCode"] == '':
        data["iataCode"] = flight_search.get_code(data["city"])
        time.sleep(2)
        data_manager.update_code(object_id=data['id'],
                            city_name=data["city"],
                            code=data["iataCode"],
                            price=data["lowestPrice"])

print("\n")
pprint(sheet_data)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for data in sheet_data:
    print(f"Flight for {data["city"]} will be generated")
    flights = flight_search.check_flight(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=data["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{data["city"]} : £{cheapest_flight.price}")
    time.sleep(2)
    # print(type(str(cheapest_flight)))
    # print(type(data["lowestPrice"]))
    if cheapest_flight.price != "N/A":
        if float(cheapest_flight.price) < data["lowestPrice"]:
            notification_manager.send_message(
                origin_city_code=ORIGIN_CITY_IATA,
                destination_city_code=data["iataCode"],
                from_time=tomorrow.strftime("%Y-%m-%d"),
                to_time=six_month_from_today.strftime("%Y-%m-%d"),
                cheapest_price=cheapest_flight.price)












