import json
import requests

api_url = 'https://api.weatherapi.com/v1/current.json?key=4b8a0843aabb40588c641045221410&q=Pakistan&aqi=no'

response = requests.get(api_url)
# print(response)
# print(response.status_code)
print(response.json())

# pak_api = str(response)

convert_bytecode = response.content.decode('UTF-8')
pak_api = json.loads(convert_bytecode)
with open('pakistan_weather_json', 'w') as pw:
    json.dump(pak_api, pw)
