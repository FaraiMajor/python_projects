import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/page-{}.html'

# req = requests.get(url.format('1'))
# soup = BeautifulSoup(req.text, 'lxml')

# get title of a book with 2 star rating
# product = soup.select('.product_pod')

# example = product[0]

# rating = example.select('a')[1]['title']

# print(rating)

f = open('books.txt', 'w')

two_star = []

for i in range(1, 51):
    scrape_url = url.format(i)
    res = requests.get(scrape_url)

    soup = BeautifulSoup(res.text, 'lxml')
    books = soup.select('.product_pod')

    for book in books:
        # if 'star-rating Two' in str(book):
        if len(book.select('.star-rating.Two')) != 0:
            two_star.append(book.select('a')[1]['title'])


for i in range(len(two_star)):
    f.write(f"{i+1}: {two_star[i]}\n")

f.close()
