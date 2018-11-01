# Filename  : beautiful.py
# Date  : 2018/10/23
import requests
import re
from lxml import etree
from bs4 import BeautifulSoup


# 取页面HTML
def get_one_page():
	url = "https://www.mkv99.net/vod-detail-id-12856.html"
	headers = {
		"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
	}
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		text = response.content.decode('utf-8')
		return text
	return None


# 解析页面
def parse_soup(html):
	# etree_html = etree.HTML(html)
	# print(etree_html)
	soup = BeautifulSoup(html, "lxml")
	print(soup.prettify())
	# print(soup.title.string)
	# print(soup.head)获取网页head所有内容
	# print(soup.p)获取第一个p标签


def main():
	html = get_one_page()
	# print(html)
	parse_soup(html)


if __name__ == '__main__':
	main()