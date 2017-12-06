from urllib.request import urlopen
from bs4 import BeautifulSoup

url = ''
r = urlopen(url).read()
soup = BeautifulSoup(r, 'html.parser')

soup.find('a', href=True)
