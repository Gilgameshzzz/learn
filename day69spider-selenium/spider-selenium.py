from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from lxml import etree

# browser = webdriver.Chrome("D:/env/chromedriver.exe")
# 无头浏览器
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.set_window_size(1000, 700)
wait = WebDriverWait(browser, 10)

KEYWORD = '电脑显示器'


def get_page(page):
	url = 'https://search.jd.com/Search?keyword=%s&enc=utf-8' % quote(KEYWORD)
	print(url)
	browser.get(url)

	# 把网页窗口垂直拉到底
	browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

	if page > 1:
		# 选择需要操作的标签或字符
		input = wait.until(
			EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
		# 执行点击操作
		submit = wait.until(
			EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))


def main():
	for page in range(100):
		page_source = get_page(page + 1)

	get_page()


if __name__ == '__main__':
	main()