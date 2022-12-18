from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/Grace_Hopper'
req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
site_para = soup.select("p")
page_title = soup.select('title')

f = open('scrap.txt', 'w')

f.write(f'{page_title[0].getText()}\n\n')

for item in soup.select(".toctext"):
    f.write(f'{item.text}\n')

for item in site_para:
    f.write(f'{item.getText()}\n')

link = soup.select('a')
for i in link:
    print(i)

for item in soup.find_all('img'):
    print(item['src'])

f.close()


# res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
# soup = BeautifulSoup(res.text, 'lxml')
# image_info = soup.select('.thumbimage')
# print(image_info)
# print(len(image_info))
# computer = image_info[0]
# print(computer)

# print(computer['src'])
