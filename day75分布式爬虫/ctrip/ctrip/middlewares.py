# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time
from logging import getLogger

from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scrapy import signals


class CtripSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class CtripDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def __init__(self, timeout):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('user-agent="Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US)'
                                    ' AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16"')
        self.browser = webdriver.Chrome(chrome_options=chrome_options)

        self.browser.set_window_size(1200, 750)
        self.browser.set_page_load_timeout(timeout)

        self.wait = WebDriverWait(self.browser, timeout)

    def __del__(self):
        self.browser.close()

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls(crawler.settings.get("SELENIUM_TIMEOUT"))
        # crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        self.browser.get(request.url)

        city_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#txtCity')))
        # 清空标签的字符
        city_input.clear()
        # 向标签输入字符
        city_input.send_keys('上海')

        # 日期
        checkin_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#txtCheckIn')))
        # 清空标签的字符
        checkin_input.clear()
        # 向标签输入字符
        checkin_input.send_keys('2018-12-07')

        checkout_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#txtCheckOut')))
        # 清空标签的字符
        checkout_input.clear()
        # 向标签输入字符
        checkout_input.send_keys('2018-12-14')

        room_count = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_roomCount'))
        )
        room_count.click()

        room_list = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//ul[@id="J_roomCountList"]/li[3]'))
        )
        room_list.click()

        guest_num = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="J_RoomGuestInfoTxt"]'))
        )
        guest_num.click()

        adult_count = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//span[@id="J_AdultCount"]//i[@class="icon_numplus"]'))
        )
        adult_count.click()

        child_count = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//span[@id="J_ChildCount"]//i[@class="icon_numplus"]'))
        )
        child_count.click()
        # 确定按钮
        ok = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[@id="J_RoomGuestInfoBtnOK"]'))
        )
        ok.click()
        # 搜索
        search = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="btnSearch"]'))
        )
        search.click()

        # 	查看页码是否加载完成
        # self.wait.until(
        #     EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#btnSearch::attr(value)'), '搜索'))

        return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',
                            status=200)

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
