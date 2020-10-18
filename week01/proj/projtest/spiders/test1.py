import scrapy


class Test1Spider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['test1.org']
    start_urls = ['http://test1.org/']

    def parse(self, response):
        pass
