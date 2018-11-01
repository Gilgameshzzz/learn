# Filename  : spider.py
# Date  : 2018/10/23
import requests
import re
from lxml import etree
from bs4 import BeautifulSoup


# 取页面HTML
def get_one_page():
	url = "https://book.douban.com/tag/%E7%BC%96%E7%A8%8B"
	headers = {
		"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
	}
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		text = response.content.decode('utf-8')
		return text

	return None


# 解析页面
def parse_with_xpath(html):
	etree_html = etree.HTML(html)
	names = etree_html.xpath('//div[@class="info"]/h2/a/text()')
	commit = etree_html.xpath('//div[@class="info"]/div[contains(@class,"star")]/span[@class="rating_nums"]/text()')
	book_name = []
	name = [i.strip() for i in names if i.strip()]
	for i in range(len(name)):
		book = {'书名': names[i], '评价': commit[i]}
		book_name.append(book)
		print(book)
	print(book_name)
	print(len(name))
	print(name)


def main():
	html = get_one_page()
	# print(html)
	parse_with_xpath(html)


if __name__ == '__main__':
	main()