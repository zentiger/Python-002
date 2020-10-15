import scrapy


class PhoneSpider(scrapy.Spider):
    name = 'phone'
    allowed_domains = ['www.smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/']

    def parse(self, response):

        phone_top10_comment = response.xpath("//ul[@id='feed-main-list']/li[@class='feed-row-wide']//a[@class='z-group-data']/@href")
        for url in phone_top10_comment.extract()[:10]:
            yield scrapy.Request(url,callback=self.comments_parse)

    def comments_parse(self, response):
        comments = response.xpath('//ul[@class="comment_listBox"]/li[@class="comment_list"]//span[@itemprop="description"]/text()')
        print(comments.extract()[0])
