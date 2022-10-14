import json
import requests

api_url = 'http://api.weatherapi.com/v1/current.json?key=4b8a0843aabb40588c641045221410&q=dhaka&aqi=no'

response = requests.get(api_url)
# print(response.status_code)
# print(response)
print(response.json())


# json_api = str(response)  # return the response code in string

json_api = response.content.decode('UTF-8')

json_api = json.loads(json_api)

with open('api_weather_json', 'w') as work_api:
    json.dump(json_api, work_api)