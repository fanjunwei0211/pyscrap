from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")
bsObject = BeautifulSoup(html.read(), "html.parser")

print(bsObject.h1)
