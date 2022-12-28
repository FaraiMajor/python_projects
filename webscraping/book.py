import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/catalogue/page-{}.html'
main_url = "https://quotes.toscrape.com/"

req = requests.get(main_url)
soup = BeautifulSoup(req.text, 'lxml')

# print authors use set to avoid duplicates
authors = set()
for name in soup.select(".author"):
    authors.add(name.text)
print(authors)

qoutes = []

# print qoutes
for quote in soup.select('.text'):
    qoutes.append(quote.text)

print(*qoutes, sep="\n")

# print top-ten tags
for item in soup.select(".tag-item"):
    print(item.text)

# print all authors unique values
# author = set()
# auth_url = 'https://quotes.toscrape.com/page/{}/'
# for page in range(1, 11):
#     res = requests.get(auth_url.format(page))
#     soup = BeautifulSoup(res.text, 'lxml')
#     for name in soup.select('.author'):
#         author.add(name.text)

# print(*author, sep="\n")

# use this when we dont know the number of pages available
page_still_valid = True
author = set()
page = 1

# Obtain Request
auth_url = 'https://quotes.toscrape.com/page/{}/'
while page_still_valid:

    # Concatenate to get new page URL
    page_url = auth_url.format(page)

    # Obtain Request
    res = requests.get(page_url)

    # Check to see if we're on the last page
    if "No quotes found!" in res.text:
        break

    # Turn into Soup
    soup = BeautifulSoup(res.text, 'lxml')

    # Add Authors to our set
    for name in soup.select(".author"):
        author.add(name.text)

    # Go to Next Page
    page += 1

print(*author, sep="\n")

# -------------------------------------------------------------------------------
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
