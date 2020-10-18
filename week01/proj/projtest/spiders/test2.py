import scrapy


class Test2Spider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['test1.org']
    start_urls = ['http://test1.org/']

    def parse(self, response):
        pass
