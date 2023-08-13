import requests
from datetime import date
import os
import urllib
from app import set_wallpaper

API_KEY = "zfnI22BydNBUlLxtP56gFZHhNq5BQ9bvqzZgRL7Y"
today = date.today()
image_path = "/Users/ansh/Documents/projects/wallpaper/img.jpeg"


response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&date={today}")
r = response.json()
url = r['url']
content = r['explanation']

urllib.request.urlretrieve(url, 'img.jpeg')
print(content)

set_wallpaper(image_path)
