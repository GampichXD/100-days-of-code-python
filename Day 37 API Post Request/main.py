# API Request
# GET --> You want data, system send data
# POST --> You want to make your data, system response to make it real
# PUT --> Edit & Update data
# DELETE --> Delete specific data

import requests
from datetime import datetime

USERNAME = "gampich"
TOKEN = "jdi23jei8328dha"




pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

GRAPH_ID = "graph1"
graph_config = {
    "id" : GRAPH_ID,
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "momiji"
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# today = datetime.now()
the_day = datetime(year=2025, month=3, day=17)
# print(today.strftime("%Y%m%d"))

post_pixel_config = {
    "date" : the_day.strftime("%Y%m%d"),
    # "quantity" : "8.76",
    "quantity" : input("How many kilometer did you cycle today? : ")
}

response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{the_day.strftime("%Y%m%d")}"

update_config = {
    "quantity" : "5.9"
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{the_day.strftime("%Y%m%d")}"

# response = requests.delete(url=delete_endpoint,headers=headers )
# print(response.text)