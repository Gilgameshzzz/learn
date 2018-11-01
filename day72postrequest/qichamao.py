# Filename  : qichamao.py
# Date  : 2018/10/30
import json

import pymysql
import requests
from lxml import etree

db = pymysql.connect(host='localhost', user='root', password='qwer1234', port=3306, db='spiders')


class Qichamao:

	def __init__(self):
		self.url = 'https://www.qichamao.com/cert-wall'
		self.headers = {
			'Referer': 'https://www.qichamao.com/',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
			'Host': 'www.qichamao.com'
		}
		self.session = requests.Session()

	def get_page(self):
		response = self.session.get(self.url, headers=self.headers)
		if response.status_code == 200:
			return response.content.decode('utf-8')
		else:
			return None

	def parse_html(self, html):
		selector = etree.HTML(html)
		company_list = []
		company_items = selector.xpath('//div[@class="firmwall_list_box"]')
		for company_item in company_items:
			company_dict = {}
			company_name = company_item.xpath('.//*[@class="firmwall_list_tit toe"]/a/text()')[0]
			company_dict['company_name'] = company_name
			company_list.append(company_dict)
		return company_list

	def post_page(self, page, pagesize):
		data = {'page': page, 'pagesize': pagesize}
		response = self.session.post(self.url, headers=self.headers, data=data)
		if response.status_code == 200:
			return response.content.decode('utf-8')
		else:
			return None

	def parse_json(self, json_text):
		result_json = json.loads(json_text)
		cursor = db.cursor()
		data_list = result_json['dataList']
		sql = 'insert into company(companyName, companybrief, logurl, c_name, c_position, phone, email) values(%s, %s, %s, %s, %s, %s, %s)'
		for data in data_list:
			company_name = data['CompanyName']
			c_name = data['c_name']
			c_position = data['c_position']
			phone = data['c_phone']
			email = data['c_email']
			companybrief = data['CompanyBrief'][:255]
			logourl = data['logoUrl']
			try:
				cursor.execute(sql, (company_name, companybrief, logourl, c_name, c_position, phone, email))
				db.commit()
			except:
				continue
			print(data['CompanyName'])
		return data_list


def main():
	qichamao = Qichamao()
	html = qichamao.get_page()
	result = qichamao.parse_html(html)
	# with open('company.json', 'a', encoding='utf-8') as f:
	# 	f.write(json.dumps(result, ensure_ascii=False) + '\n')
	for j in result:
		print('page 1')
		print('*' * 20)
		print(j['company_name'])

	for i in range(100):
		print('page %s' % (i+2))
		print("*" * 20)
		json_text = qichamao.post_page(i+2, 9)
		data = qichamao.parse_json(json_text)
		# with open('company.json', 'a', encoding='utf-8') as g:
		# 	g.write(json.dumps(data, ensure_ascii=False) + '\n')


if __name__ == '__main__':
	main()