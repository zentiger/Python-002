import scrapy


class Test3Spider(scrapy.Spider):
    name = 'test3'
    allowed_domains = ['test1.org']
    start_urls = ['http://test1.org/']

    def parse(self, response):
        pass
