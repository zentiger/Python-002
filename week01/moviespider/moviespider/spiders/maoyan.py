import scrapy
from moviespider.items import MaoyanMovieItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    #start_urls = ['http://maoyan.com/']

    def start_requests(self):
        urls = ["https://maoyan.com/films?showType=3"]
        cookies = {
            'uuid_n_v':'v1', 
            'uuid':'D3F3ABB0CCFF11EAB0594FFAA70EE9CE992E7740FAFC4FA3AC3E78578E17132B',
            '_csrf':'4b94dc7d886b67d5d98ac3cd92ae54756deb0929701149927efbd4feb072ce4e',
            '_lxsdk_cuid':'1737c75fe2cc8-065a78fe4d7979-31617402-232800-1737c75fe2cc8',
            '_lxsdk':'D3F3ABB0CCFF11EAB0594FFAA70EE9CE992E7740FAFC4FA3AC3E78578E17132B',
            'mojo-uuid': '7137f97ef2cc97290d1dc1d484a19007',
            'mojo-session-id':'{"id":"f1a20cfcc9425b43f41e2246ae214dd8","time":1595520975197}',
            'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2':'1595520975,1595520988',
            'mojo-trace-id':'12',
            'Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2':'1595521026',
            '__mta':'146519947.1595520975189.1595521015332.1595521026460.8', 
            '_lxsdk_s':'1737c75fe2d-9f-ab2-76c%7C%7C21'
        }


        for url in urls:
            yield scrapy.Request(url=url, cookies = cookies, callback=self.parse)

    def parse(self, response):
        count = 0
        items = []
        for movie_info in response.xpath("//div[@class='movie-hover-info']"):
            divs = movie_info.xpath('./div[@class="movie-hover-title"]')
            movie_name = divs[0].xpath('./span[@class="name"]/text()').get()
            if not movie_name:
                movie_name = divs[0].xpath('./span[@class="name "]/text()').get()

            movie_type = divs[1].xpath('./text()').getall()[1].strip()
            try:
                movie_showtime = divs[3].xpath('./text()').getall()[1].strip()
            except:
                divs = movie_info.xpath('./div[@class="movie-hover-title movie-hover-brief"]')
                movie_showtime = divs.xpath('./text()').getall()[1].strip()
            item = MaoyanMovieItem()
            item['movie_name'] = movie_name
            item['movie_type'] = movie_type
            item['movie_showtime'] = movie_showtime
            items.append(item)
            count += 1 
            if count >= 10:
                break

        return items            