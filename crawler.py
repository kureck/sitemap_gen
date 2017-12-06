from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# get url
# check if url is valid
# check if is same host
# check if it was not visited yet. Maybe a dict to do that
# call crawler for those valid links

class Crawler:

    def __init__(self, url):
        self.url = url
        self.host = urlparse(url).netloc

    def crawl(self, url):
        r = urlopen(url).read()
        soup = BeautifulSoup(r, 'html.parser')

        soup.find('a', href=True)

    def valid(self, url):
        parsed = urlparse(url)

        if url != '' or parsed.scheme in ['http', 'https', '']:
            return True
        return False

    def same_host(self, url):
        host = urlparse(url).netloc

        return self.host == host
