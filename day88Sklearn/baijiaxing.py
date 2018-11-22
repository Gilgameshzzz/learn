# Filename  : baijiaxing.py
# Date  : 2018/11/21


# 取页面HTML
import pymysql
import requests
from lxml import etree

# 连接数据库
db = pymysql.connect(host='localhost', user='root', password='qwer1234', port=3306, db='hundredname')


def get_one_page(url="http://www.resgain.net/xmdq.html"):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
	}
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		text = response.content.decode('utf-8')
		return text

	return None


def parse_with_xpath(html):
	# 解析页面
	etree_html = etree.HTML(html)
	# 获取姓的链接
	names = etree_html.xpath('/html/body/div[3]/div/div/div[2]/a/@href')
	# 整理链接
	name = [i.strip() for i in names if i.strip()]

	return name


def save_link(links):
	# 把链接写入txt文件
	for link in links:
		link = link.split('//')[1]
		with open('baijiaxing.txt', 'a', encoding='utf-8') as g:
			g.write(link + '\n')
	return '写入成功'


def parse_name(html):
	# 解析页面
	etree_html = etree.HTML(html)
	Name = etree_html.xpath('/html/body/div[2]/div/div[4]/div[2]/div[1]/div[1]/h3/text()')[0].split(':')
	name = Name[1]
	five_elements = etree_html.xpath('/html/body/div[2]/div/div[4]/div[2]/div[1]/div[2]/div[1]/blockquote/text()')[0]
	sancai = etree_html.xpath('/html/body/div[2]/div/div[4]/div[2]/div[1]/div[2]/div[2]/blockquote/text()')[0]
	Namewuge = etree_html.xpath('/html/body/div[2]/div/div[4]/div[2]/div[1]/div[2]/div[3]/blockquote/text()')
	namewuge = ''.join([i.strip() for i in Namewuge if i.strip()])
	Tiange = etree_html.xpath('/html/body/div[2]/div/div[4]/div[2]/div[1]/div[2]/div[4]/blockquote/div[1]/text()')[0]
	tiange = Tiange.split('：')[1]
	Renge = etree_html.xpath('/html/body/div[2]/div/div[4]/div[2]/div[1]/div[2]/div[4]/blockquote/div[2]/text()')[0]
	renge = Renge.split('：')[1]
	Dige = etree_html.xpath('/html/body/div[2]/div/div[4]/div[2]/div[1]/div[2]/div[4]/blockquote/div[3]/text()')[0]
	dige = Dige.split('：')[1]
	Waige = etree_html.xpath('/html/body/div[2]/div/div[4]/div[2]/div[1]/div[2]/div[4]/blockquote/div[4]/text()')[0]
	waige = Waige.split('：')[1]
	Zongge = etree_html.xpath('/html/body/div[2]/div/div[4]/div[2]/div[1]/div[2]/div[4]/blockquote/div[5]/text()')[0]
	zongge = Zongge.split('：')[1]
	First_name = etree_html.xpath('//*[@id="navbar-main"]/ul[1]/li[6]/a/text()')[0]
	first_name = First_name.split('姓')[0]
	info = [first_name, name, five_elements, sancai, namewuge, tiange, renge, dige, waige, zongge]
	save_sql(info)
	return


def save_sql(info):
	# 存入mysql
	cursor = db.cursor()
	sql = 'insert into names(first_name, Name, the_five_elements, sancaipeizhi, namewuge, tiange, renge, dige, waige, zongge) values("%s", "%s","%s", "%s", "%s", "%s", "%s", "%s","%s","%s")' % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8], info[9])
	try:
		cursor.execute(sql)
		db.commit()
		print('=======' + info[1])
	except:
		print('已有该姓名')


def deep_parse():
	with open('baijiaxing.txt', 'r') as f:
		links = f.read()

	link = links.split('\n')
	# 读取链接
	for l in link:
		link = 'http://' + l
		for j in range(10):
			if 'zhou' in link:
				j += 4
			else:
				j += 1
			alink = link.split('.html')
			num_link = alink[0] + '_' + str(j) + '.html'
			# 打开链接
			html = get_one_page(num_link)
			etree_html = etree.HTML(html)
			# 获取名字
			names = etree_html.xpath('/html/body/div[3]/div[2]/div[1]/div/a/text()')
			if names[0].strip():
				for name in names:
					# 获取姓名详情链接
					new_link = num_link.split('_list')[0] + '/' + name + '.html'
					# 打开姓名详情链接
					new_html = get_one_page(new_link)
					parse_name(new_html)


def main():
	# html = get_one_page()
	# print(html)
	# all_link = parse_with_xpath(html)
	# save_link(all_link)
	deep_parse()
	db.close()


if __name__ == '__main__':
	main()
