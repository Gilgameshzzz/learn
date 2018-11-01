# Filename  : mogujie.py
# Date  : 2018/10/24
import json

import pymysql
import requests
import re
from lxml import etree
from bs4 import BeautifulSoup

# 连接数据库
db = pymysql.connect(host='localhost', user='root', password='qwer1234', port=3306, db='spiders')


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


def get_real_content(html):
	if html and len(html) > 128:
		i = html.index('(')
		html1 = html[i+1:]
		# html1 = html.split('(')[1:][0]
		# print(len(html1))
		html1 = html1.replace(');', '')
		return html1
	return None


def main():
	j = 1
	while True:
		j += 1
		url = 'https://list.mogujie.com/search?callback=jQuery21105824885541937317_1540350434480&_version=8193&cKey=15&page=%s&ad=0&action=boyfriend&_=154035043448%s' % (j, j)
		html = get_one_page(url)
		# print(html)
		html2 = get_real_content(html)
		result = json.loads(html2)
		# with open('mogujie.json', 'a', encoding='utf-8')as g:
		# 	g.write(json.dumps(result))
		clothes = result['result']['wall']['docs']
		cursor = db.cursor()
		sql = 'insert into clothes(title, img, orgPrice, price, sale, cfav, tradeItemId) values(%s, %s, %s, %s, %s, %s, %s)'
		# sql = 'update clothes set tradeItemId=%s where id=%s' 更新数据库，在已有表格数据后面加字段并加入数据
		for i in range(len(clothes)):
			title = clothes[i]['title']
			img = clothes[i]['img']
			orgPrice = clothes[i]['orgPrice']
			price = clothes[i]['price']
			sale = clothes[i]['sale']
			cfav = clothes[i]['cfav']
			tradeItemId = clothes[i]['tradeItemId']
			try:
				cursor.execute(sql, (title, img, orgPrice, price, sale, cfav, tradeItemId))
				db.commit()
			except:
				db.rollback()
				continue

		print(j)
		if result['result']['wall']['isEnd']:
			db.close()
			break


def read_json():
	with open('mogujie.json', 'r', encoding='utf-8') as j:
		info = json.load(j)
	clothes = info['result']['wall']['docs']
	print(clothes)


def put_mysql():
	cursor = db.cursor()
	sql = "CREATE TABLE 'clothes' ('id' int(11) NOT NULL AUTO_INCREMENT," \
	      "'title' varchar(255) DEFAULT NULL,'img' varchar(255) DEFAULT NULL," \
	      "'orgPrice' int(11) DEFAULT NULL,'price' int(11) DEFAULT NULL,'sale' int(11) DEFAULT NULL," \
	      "'cfav' int(11) DEFAULT NULL,'tradeItemId' varchar(255) DEFAULT NULL,PRIMARY KEY ('id')," \
	      "UNIQUE KEY 'ux_clothes' ('tradeItemId')) ENGINE=InnoDB AUTO_INCREMENT=5410 DEFAULT CHARSET=utf8;"
	print(sql)
	cursor.execute(sql)
	db.close()


def insert_info():
	with open('mogujie.json', 'r', encoding='utf-8') as j:
		info = json.load(j)
	clothes = info['result']['wall']['docs']
	cursor = db.cursor()
	sql = 'insert into clothes(title, img, orgPrice, price, sale, cfav, tradeItemId) values(%s, %s, %s, %s, %s, %s, %s)'

	# sql = 'update clothes set tradeItemId=%s where id=%s' 更新数据库，在已有表格数据后面加字段并加入数据
	for i in range(len(clothes)):
		title = clothes[i]['title']
		img = clothes[i]['img']
		orgPrice = clothes[i]['orgPrice']
		price = clothes[i]['price']
		sale = clothes[i]['sale']
		cfav = clothes[i]['cfav']
		tradeItemId = clothes[i]['tradeItemId']
		# try:
		cursor.execute(sql, (title, img, orgPrice, price, sale, cfav, tradeItemId))
		db.commit()
		# except:
		# 	continue
	db.close()
	print(len(clothes))


if __name__ == '__main__':
	main()