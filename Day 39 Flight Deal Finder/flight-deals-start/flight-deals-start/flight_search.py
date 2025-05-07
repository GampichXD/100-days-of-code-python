import os
import requests
from dotenv import load_dotenv
import time
AMADEUS_ENDPOINT = "https://test.api.amadeus.com/v1"
AMADEUS_ENDPOINT_2 = "https://test.api.amadeus.com/v2"
load_dotenv()





class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ["API_KEY"]
        self._api_secret = os.environ["API_SECRET"]
        self._token = self._get_new_token()
        pass
    def get_code(self, city: str):
        headers = {
            "Authorization": f"Bearer {self._token}",
        }
        city_params = {
            "keyword" : city.capitalize(),
            "max": "2",
            "include": "AIRPORTS",
        }
        count_entry = 0
        limit_entry = 3

        while count_entry < limit_entry:
            print(f"Attempt {count_entry + 1}/{limit_entry} for city: {city}.")
            response = requests.get(url=f"{AMADEUS_ENDPOINT}/reference-data/locations/cities", params=city_params, headers=headers)
            if response.status_code == 200:
                try:
                    response_data = response.json()
                    if "data" in response_data and response_data["data"]:
                        return response_data["data"][0]["iataCode"]
                    else:
                        print(f"No IATA code found for city: {city}.")
                        return ''
                except (KeyError, IndexError) as e:
                    print(f"Error parsing response for city {city}: {e}")
                    return ''
            else:
                print("Something wrong about the server. Try to request again!")
                time.sleep(5)
                count_entry += 1
        print("Oh no, you reach rate limit. Try another account")
        return None

    def _get_new_token(self):
        amadeus_params = {
            "grant_type": "client_credentials",
            "client_id" : self._api_key,
            "client_secret" : self._api_secret
        }
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(url=f"{AMADEUS_ENDPOINT}/security/oauth2/token", data=amadeus_params, headers=header)
        if response.status_code == 200:
            the_token = response.json()["access_token"]
            # print(the_token)
            return the_token
        else:
            print(response.text)
            return None
        # print(response.text)
        # print(type(response.text))
        # return response["access_token"]
        # pass

    def check_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(url=f"{AMADEUS_ENDPOINT_2}/shopping/flight-offers",
                                headers=headers,
                                params=query)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None
    # pass


# test = FlightSearch()
# print(test.get_code("KUALA LUMPUR"))
