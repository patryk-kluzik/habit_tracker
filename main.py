import requests
import datetime

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'

USERNAME = "basedpole"
TOKEN = "poopparty69"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

"""
Ran at the start to create the user
"""
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)


GRAPH_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs'
GRAPH_ID = "swimgraph1"

graph_params = {
    "id": GRAPH_ID,
    "name": "Swimming Graph",
    "unit": "laps",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
"""
run once to create the graph
"""
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(response.text)

POST_PIXEL_ENDPOINT = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}'
today_date_formatted = datetime.datetime.today().strftime("%Y%m%d")

# pixel_params = {
#     "date": today_date_formatted,
#     "quantity": input("How many laps did you swim today?")
# }

UPDATE_PIXEL_ENDPOINT = f'{POST_PIXEL_ENDPOINT}/{today_date_formatted}'

update_params = {
    "quantity": "25"
}

"""
run to add pixel to the graph
"""
# response = requests.post(url=POST_PIXEL_ENDPOINT, json=pixel_params, headers=headers)
# print(response.text)

"""
run to update pixel to the graph
"""
# response = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=update_params, headers=headers)
# print(response.text)
"""
run to delete pixel to the graph
"""
# response = requests.delete(url=UPDATE_PIXEL_ENDPOINT, headers=headers)
# print(response.text)

"""
View the graph
"""

VIEW_PIXEL_ENDPOINT = f'http://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}.html'

import webbrowser

webbrowser.open(url=VIEW_PIXEL_ENDPOINT)