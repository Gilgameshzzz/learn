# -*- coding: utf-8 -*-
import scrapy

from movies.items import MoviesItem


class FirmSpider(scrapy.Spider):
    name = 'firm'
    allowed_domains = ['idyjy.com']
    start_urls = ['http://www.idyjy.com/sub/']

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,mt;q=0.2',
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'www.idyjy.com',
        }
        for i in range(27221, 27226):
            yield scrapy.Request(
                url='http://www.idyjy.com/sub/%s.html' % i,
                headers=headers,
                method='GET',
                callback=self.parse
            )

    def yield_info(self, item):
        yield item

    def parse(self, response):
        firm_item = MoviesItem()
        info = response.xpath('//div[@class="box"]/h3/text()').extract_first()
        if info:
            print('该网页没有内容')
        else:
            name = response.xpath('//span[@id="name"]/text()').extract_first()
            # 年份有问题
            years = response.xpath('//div[@class="info"]/ul/li').re('\d{4}')[0]

            category = response.xpath('//div[@class="location"]/a[3]/text()').extract_first()
            # 链接有问题
            down_url = response.xpath('//div[@class="down_list"]')
            if len(down_url) > 1:
                down_url = down_url[-1]

            movies_down_url = down_url.xpath('./ul/li/input/@value').extract()

            for movie_down_url in movies_down_url:
                firm_item['name'] = name
                firm_item['years'] = years
                firm_item['category'] = category
                firm_item['down_url'] = movie_down_url
                yield firm_item
