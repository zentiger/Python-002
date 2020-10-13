import scrapy


class PhoneSpider(scrapy.Spider):
    name = 'phone'
    allowed_domains = ['www.smzdm.com']
    start_urls = ['http://www.smzdm.com/']

    def parse(self, response):
        pass
