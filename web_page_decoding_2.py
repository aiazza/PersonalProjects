# Source : https://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html
# Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on the website : url = 'https://www.cprime.com/resources/blog/what-are-the-benefits-of-network-automation/#:~:text=Network%20automation%20removes%20all%20those,processes%20more%20flexible%20and%20agile.'
# The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.
# (Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries through the solution of the exercise posted here.)
# This will just print the full text of the article to the screen. It will not make it easy to read, so next exercise we will learn how to write this text to a .txt file.



import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.cprime.com/resources/blog/what-are-the-benefits-of-network-automation/#:~:text=Network%20automation%20removes%20all%20those,processes%20more%20flexible%20and%20agile.'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html,'html.parser')
titles = soup.find_all('p') 

for title in titles:
    print(title.text)