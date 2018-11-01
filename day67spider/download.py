# Filename  : download.py
# Date  : 2018/10/23
import json

import pymysql
import requests
import re
from lxml import etree
from bs4 import BeautifulSoup


db = pymysql.connect(host='localhost', user='root', password='qwer1234', port=3306)
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchall()
# print('Database version:', data)
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
# db.close()


# 取页面HTML
def get_one_page(url):

	headers = {
		"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
	}
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		text = response.content.decode('utf-8')
		return text
	return None


# 解析页面 boss直聘网 python信息
def parse_soup(html):
	# etree_html = etree.HTML(html)
	# print(etree_html)
	soup = BeautifulSoup(html, "lxml")
	places = soup.select('.info-primary p')
	jobs = soup.select('.job-title')
	prices = soup.select('.red')
	job_infos = []
	for i in range(len(places)):
		job_info = {}
		job_info['地点'] = (list(places[i].stripped_strings)[0])
		job_info['职位'] = (list(jobs[i].stripped_strings)[0])
		job_info['月工资'] = (list(prices[i].stripped_strings)[0])
		job_infos.append(job_info)
	with open('boss.json', 'a', encoding='utf-8') as g:
		g.write(json.dumps(job_infos, ensure_ascii=False)+'\n')

	print(job_infos)


	# index = soup.prettify()
	# with open('a.txt', 'w', encoding='utf-8') as g:
	# 	g.write(index)


def main():
	# for i in range(10):
	# 	i += 1
	url = "https://search.jd.com/search?keyword=%E7%94%B5%E8%84%91%E6%98%BE%E7%A4%BA%E5%99%A8&enc=utf-8&page=5"
	html = get_one_page(url)
	etree_html = etree.HTML(html)
	names = etree_html.xpath('//li[@class="gl-item"]/div/div[contains(@class,"p-name p-name-type-2")]/a/em/text()')
	img = etree_html.xpath('//li[@class="gl-item"]/div/div[@class="p-price"]')
	prices = etree_html.xpath('//li[@class="gl-item"]/div/div[@class="p-price"]/strong/i/text()')
	comment = etree_html.xpath('//li[@class="gl-item"]/div/div[@class="p-commit"]/a/text()')
	goods_id = etree_html.xpath('//li[@class="gl-item"]/@data-sku')
	print(goods_id)
	print(len(goods_id))
	# parse_soup(html)


if __name__ == '__main__':
	main()