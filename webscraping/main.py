from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Grace_Hopper'
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
# print(soup.text)
# print(soup.select('.toctext'))
for item in soup.select(".toctext"):
    print(item.text)
