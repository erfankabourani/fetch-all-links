import requests as re
from bs4 import BeautifulSoup

url = input("Enter Link: ")
if ("https" or "http") in url:
    data = re.get(url)
else:
    data = re.get("https://" + url)
soup = BeautifulSoup(data.text, "html.parser")
links = []
for link in soup.find_all("a"):
    links.append(link.get("href"))

with open("mylinks.txt" , 'a') as saved:
    print(links[:10] , file=saved)
