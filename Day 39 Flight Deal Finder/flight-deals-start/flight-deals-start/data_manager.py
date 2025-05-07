import requests
import os
from dotenv import load_dotenv

load_dotenv()


SHEET_ENDPOINT = "https://api.sheety.co/c96619069dc1ad198961d99213396425/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.token = os.environ["TOKEN"]
        self.headers = {
            "Authorization": self.token,
        }
        response = requests.get(url=SHEET_ENDPOINT, headers=self.headers)
        data = response.json()
        self.data = data

        # pprint(self.data)
        # pass
    def update_code(self, object_id, city_name, code, price):
        update_params = {
            "price" : {
                "city" : city_name.title(),
                "iataCode" : code,
                "lowestPrice" : price,
            }
        }
        response = requests.put(url=f"{SHEET_ENDPOINT}/{object_id}", json=update_params, headers=self.headers)
    # pass

# test = DataManager()