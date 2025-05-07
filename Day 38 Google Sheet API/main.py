import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os


# Nutritionix Configuration
APP_ID = os.environ["APP_ID"]  # Raises exception if key does not exist
API_KEY = os.environ.get("API_KEY")  # Returns None if key does not exist
NUTRITIONIX_ENDPOINT = os.environ.get("NUTRITIONIX_ENDPOINT")
HOST_DOMAIN = os.environ.get("HOST_DOMAIN")

# Sheety Configuration
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")

# Basic Authentication Configuration
USERNAME = os.environ.get("USERNAME", "default_username")
PASSWORD = os.environ.get("PASSWORD", "default_password")

# Bearer Token Configuration
TOKEN = os.environ.get("TOKEN", "default_token")

basic = HTTPBasicAuth(USERNAME,PASSWORD)

nutritionix_headers = {
    # "Content-Type" : "application/json",
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY,
}

nutritionix_param = {
    "query" : input("Tell me which exercises you did: ")
}

nutri_response = requests.post(url=f"{HOST_DOMAIN}{NUTRITIONIX_ENDPOINT}", json=nutritionix_param, headers=nutritionix_headers)
result = nutri_response.json()["exercises"]

print(nutri_response.text)

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")
# print(result["user_input"].title())

headers = {
    "Authorization" : TOKEN
}

for data in result:
    sheet_param = {
            "workout" : {
                "date" : date,
                "time" : time,
                "exercise" : data["name"].title(),
                "duration" : data["duration_min"],
                "calories" : data["nf_calories"],
            }
    }

    sheet_response = requests.post(
        url=SHEET_ENDPOINT,
        json=sheet_param,
        # auth=basic,
        headers=headers,
    )

    print(sheet_response.text)









