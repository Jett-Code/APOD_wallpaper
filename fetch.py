import requests
from datetime import date
import os
import urllib
from app import set_wallpaper

API_KEY = "zfnI22BydNBUlLxtP56gFZHhNq5BQ9bvqzZgRL7Y"
today = date.today()



response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}&date=2023-08-03")
r = response.json()
url = r['url']

file_name = url.split('/')[-1]

content = r['explanation']

print("url    ->> " + url)

urllib.request.urlretrieve(url, file_name)
print(content)

image_path = f"/Users/ansh/Documents/projects/wallpaper/{file_name}"
set_wallpaper(image_path)
