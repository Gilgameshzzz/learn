# Filename  : maoyan.py
# Date  : 2018/10/22
import json

import requests
import re

"""
re.S作用：正则表达式中，“.”的作用是匹配除“\n”以外的任何字符，
也就是说，它是在一行中进行匹配。这里的“行”是以“\n”进行区分的。
字符串有每行的末尾有一个“\n”，不过它不可见。

如果不使用re.S参数，则只在每一行内进行匹配，如果一行没有，
就换下一行重新开始，不会跨行。而使用re.S参数以后，
正则表达式会将这个字符串作为一个整体，将“\n”当做一个普通的字符加入到这个字符串中，
在整体中进行匹配。
"""


def get_page(url):
	headers = {
		"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",

	}
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		# content 字节流
		return response.content.decode('utf-8')
	return None


def parse_page(html):
	# 获取电影名
	pattern1 = re.compile('movieId.*?>.*?<img.*?<img.*?alt="(.*?)" class', re.S)
	# 获取主演信息
	pattern2 = re.compile('<p class="star">(.*?)</p>', re.S)
	# 获取上映时间
	pattern3 = re.compile('<p class="releasetime">(.*?)</p> ', re.S)
	# 获取排名
	pattern4 = re.compile('<i class="board-index board-index-(.*?)"', re.S)
	# 获取电影海报
	# pattern5 = re.compile('<img data-src="(.*?)" alt="', re.S)
	movie_name = re.findall(pattern1, html)
	actor = re.findall(pattern2, html)
	time = re.findall(pattern3, html)
	rank = re.findall(pattern4, html)
	# item5 = re.findall(pattern5, html)
	movie_info = []
	for i in range(len(movie_name)):
		info = {'movie_name': movie_name[i].strip(), 'actor': actor[i].strip(), 'releasetime': time[i].strip(), 'rank': rank[i].strip()}
		movie_info.append(info)
	print(movie_info)
	return movie_info


# def get_movie(html):
	# pattern = re.compile(
	# 	'data-val=.*?>(.*?)</a>.*<p class="star">(.*?)</p>.*<p class="releasetime">(.*?)</p>.*><i class="integer">(.*?)</i><i class="fraction">(.*)</i><'
	# )
	# item = re.findall(pattern, html)
	# print(item)
	# return item


def save_img(url):
	img_url = url.split('@')[0]
	file_name = img_url.split("/")[-1]
	with open('.\img\%s' % file_name, 'wb') as f:

		response = requests.get(url)
		f.write(response.content)


def save_json(dict):
	with open('movie.json', 'a', encoding='utf-8') as g:
		g.write(json.dumps(dict, ensure_ascii=False))


def main():
	url = 'https://maoyan.com/board/4?offset='
	for i in range(0, 100, 10):
		new_url = url + str(i)
		html = get_page(new_url)
		items = parse_page(html)
		save_json(items)


if __name__ == '__main__':
	main()
