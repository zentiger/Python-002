import scrapy
from PhoneSpider.items import PhonespiderItem
from snownlp import SnowNLP

class PhoneSpider(scrapy.Spider):
    name = 'phone'
    allowed_domains = ['www.smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/']

    def parse(self, response):

        phone_top10_comment = response.xpath("//ul[@id='feed-main-list']/li[@class='feed-row-wide']//a[@class='z-group-data']/@href")
        for url in phone_top10_comment.extract()[:10]:
            yield scrapy.Request(url,callback=self.comments_parse)

    def next_page(self, url):
        print(url)

        if url:
            yield scrapy.Request(url=url, callback=self.comments_parse)

    def comments_parse(self, response):
        items = []
        comments = response.xpath('//ul[@class="comment_listBox"]/li[@class="comment_list"]')
        goods_title = response.xpath('//h1[@class="title J_title"]/text()').extract()[0].strip()
        for comment in comments:
            comment_id = comment.xpath('.//div[@class="comment_con"]/input/@comment-id').extract()[0]
            comment_date = comment.xpath('.//div[@class="time"]/meta/@content').extract()[0]
            comment_description = comment.xpath('.//span[@itemprop="description"]/text()').extract()[0]
            print(goods_title,comment_id, comment_date, comment_description)
            item = PhonespiderItem()
            item["goods_title"] = goods_title
            item["comment_id"] = comment_id
            item["comment_date"] = comment_date
            item["comment_description"] = comment_description
            item["comment_sentiments"] = SnowNLP(comment_description).sentiments
            items.append(item)

        next_page = response.xpath('//div[@class="comment-tab-box z-clearfix"]/ul[@class="pagination"]/li[@class="pagedown"]/a/@href').extract()
        if next_page:
            next_page_url = next_page[0]
            #yield scrapy.Request(url=next_page_url, callback=self.comments_parse)
        return items
