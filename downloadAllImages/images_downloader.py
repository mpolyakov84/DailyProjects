# app download all Images from a URL with Python
import requests
import bs4

# todo func that get all links to images
# todo func for downloading images

url = 'https://en.wikipedia.org/wiki/Tomato'
r = requests.get(url)

bs = bs4.BeautifulSoup(r.text, 'html.parser')

for img in bs.find_all('img'):
    if 'upload.wikimedia.org' in img.get('src'):
        print(f'https:{img.get('src')}')