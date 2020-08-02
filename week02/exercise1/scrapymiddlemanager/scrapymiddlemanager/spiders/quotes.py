import scrapy
from scrapymiddlemanager.items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']

    def start_requests(self):
        start_urls = ['http://quotes.toscrape.com/']

        for url in start_urls:
            yield scrapy.Request(url, callback=self.parse, meta = {"proxy": "http://161.117.191.190:404"})

    def parse(self, response):
        for quote in response.css('div.quote'):
            try:
                item = QuotesItem()
                item["author"] = quote.css('small.author::text').get()
                item["quotes"] = quote.xpath('./span[@class="text"]/text()').get().strip('“').strip('”')
            except Exception as e:
                print(e)
                continue
            yield item
         
        next_page = response.css('li.next a::attr(href)').get()
        count = 0 
        if next_page is not None and count < 10 :
            #next_page = response.urljoin(next_page)
            #yield scrapy.Request(next_page, callback = self.parse)
            count += 1
            yield response.follow(next_page, callback = self.parse, meta = {"proxy": "http://161.117.191.190:404"})
            