from sitemap_gen.crawler import Crawler


class TestCrawler:
    def setup(self):
        url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
        self.crawler = Crawler(url)

    def test_valid_url_https(self):
        url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
        expected = True
        value = self.crawler.valid(url)

        assert expected == value

    def test_valid_url_http(self):
        url = 'http://en.wikipedia.org/wiki/Python_(programming_language)'
        expected = True
        value = self.crawler.valid(url)

        assert expected == value

    def test_valid_url_same_path(self):
        url = '/wiki/Python_(programming_language)'
        expected = True
        value = self.crawler.valid(url)

        assert expected == value

    def test_valid_blank_url(self):
        url = ''
        expected = True
        value = self.crawler.valid(url)

        assert expected == value

    def test_same_host(self):
        url = 'http://en.wikipedia.org/wiki/Python_(programming_language)'

        expected = True
        value = self.crawler.same_host(url)

        assert expected == value
