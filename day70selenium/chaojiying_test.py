# Filename  : chaojiying_test.py
# Date  : 2018/10/26
import time
from io import BytesIO

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from lxml import etree
from PIL import Image

from chaojiying import main1

chrome_options = webdriver.ChromeOptions()

browser = webdriver.Chrome(chrome_options=chrome_options)

browser.set_window_size(1200, 850)
wait = WebDriverWait(browser, 10)


def get_page():
	url = "http://bm.e21cn.com/log/reg.aspx"
	browser.get(url)
	html = browser.page_source
	return html


# 取浏览器窗口全图
def get_big_image():
	"""
	获取网页截图
	:return: 截图对象
	"""
	# browser.execute_script('window.scrollTo(0, 300)')
	screenshot = browser.get_screenshot_as_png()
	screenshot = Image.open(BytesIO(screenshot))
	return screenshot


#   取浏览器窗口验证码位置
def get_position():
	img = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#imgCheckCode')))
	loc = img.location
	size = img.size
	print(img)
	print(loc)
	print(size)
	top, bottom, left, right = (loc['y']), (loc['y'] + size['height']), loc['x'], loc['x'] + size[
		'width']
	return (top, bottom, left, right)


def parse_html(name):

	screenshot = get_big_image()
	screenshot.save('full.png')
	top, bottom, left, right = get_position()
	crop_img = screenshot.crop((left, top, right, bottom))
	path = name
	crop_img.save(path)
	return crop_img


def get_masg(html):
	etree_html = etree.HTML(html)
	username = 'lalala'
	password = '123456'
	tel = '18011405897'
	img_url = etree_html.xpath('//img[@id="imgCheckCode"]/@src')
	check_url = 'http://bm.e21cn.com' + img_url[0][2:]
	img = parse_html('100.png')
	print(img)
	check_msg = main1('100.png')
	print(check_msg)
	input_username = wait.until(
		EC.presence_of_element_located((By.CSS_SELECTOR, 'input#username')))

	input_password1 = wait.until(
		EC.presence_of_element_located((By.CSS_SELECTOR, 'input#pwd')))

	input_password2 = wait.until(
		EC.presence_of_element_located((By.CSS_SELECTOR, 'input#pwd_Q')))

	input_tel = wait.until(
		EC.presence_of_element_located((By.CSS_SELECTOR, 'input#tel')))

	input_check = wait.until(
		EC.presence_of_element_located((By.CSS_SELECTOR, 'input#CheckCode')))

	sublime = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#btn_login')))
	input_username.send_keys(username)
	input_password1.send_keys(password)
	input_password2.send_keys(password)
	input_tel.send_keys(tel)
	input_check.send_keys(check_msg)
	time.sleep(2)
	sublime.click()


def main():
	html = get_page()
	get_masg(html)
	time.sleep(30)
	browser.close()


if __name__ == '__main__':
	main()