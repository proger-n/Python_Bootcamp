from bs4 import BeautifulSoup
import requests
url = "https://en.wikipedia.org/wiki/Six_degrees_of_separation"
contents = requests.get(url).text
soup = BeautifulSoup(contents, 'html.parser')
# print(soup.prettify())  # display whole html page
items = soup.find_all(class_='div-col')
it = items[0].find_all("a")
print(*it, sep="\n")
hrefs = []
for item in it:
    hrefs.append(item.get("href"))
print(*hrefs, sep="\n")
