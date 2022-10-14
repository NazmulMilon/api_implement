import json
import requests
# import PyWallpaper

api_url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'

get_data = requests.get(api_url)


api_convert = get_data.content.decode('UTF-8')
api_dict = json.loads(api_convert)
# print(get_data)
# print(api_dict)

image_url = api_dict['url']
get_image = requests.get(image_url)
# print(get_image)


with open('image.png', 'wb') as nasa_api:
    # json.dump(get_image, nasa_api)
    nasa_api.write(get_image.content)

# PyWallpaper.change_wallpaper('/home/uzzal/milon/API_implement/image.png')
