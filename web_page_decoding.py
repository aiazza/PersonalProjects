# Source : https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html
# Note: this is a 4-chili exercise, not because it introduces a concept (although it introduces a new library), but because this exercise is more like a project. Feel free to skip this and come back when you’re more ready!
# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.


import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html,'html.parser')
titles = soup.find_all('h3') 

for title in titles:
    print(title.text)