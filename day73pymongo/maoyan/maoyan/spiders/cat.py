# -*- coding: utf-8 -*-
import scrapy

from maoyan.items import MaoyanItem


class CatSpider(scrapy.Spider):
	name = 'cat'
	# 允许爬的网址
	allowed_domains = ['maoyan.com']
	start_urls = ['http://www.maoyan.com/board/4']

	def start_requests(self):
		headers = {
			'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
			'Accept': 'application/json, text/plain, */*',
			'Accept-Encoding': 'gzip, deflate, sdch',
			'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,mt;q=0.2',
			'Connection': 'keep-alive',
			'X-Requested-With': 'XMLHttpRequest',
			'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
		}
		for i in range(10):
			yield scrapy.Request(
				url='http://maoyan.com/board/4?offset=%d' % (i * 10),
				headers=headers,
				method='GET',
				callback=self.parse
			)

	def parse(self, response):
		movies = response.selector.xpath('//div[@class="board-wrapper"]/dd')
		for movie in movies:
			movie_item = MaoyanItem()

			movie_div = movie.xpath('.//div[@class="movie-item-info"]')
			movie_item['name'] = movie_div.xpath('/p[1]/a/text()').extract_first().strip()
			# movie_item['actor'] = movie_div.xpath(
			# 	'./p[@class="star"]/text()').extract_first().strip()
			# movie_item['release_time'] = movie_div.xpath(
			# 	'./p[@class="releasetime"]/text()').extract_first().strip()
			# first_score = movie_div.xpath(
			# 	'./div[@class="movie-item-number score-num"]/p/i[1]/text()').extract_first()
			# second_score = movie_div.xpath(
			# 	'./div[@class="movie-item-number score-num"]/p/i[2]/text()').extract_first()
			# movie_item['score'] = ('%s%s' % (first_score, second_score)).strip()

			yield movie_item

