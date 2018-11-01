# Filename  : 1kkk.py
# Date  : 2018/10/29
import time
from io import BytesIO
import os
import requests
import cv2

import numpy as np
from PIL import Image


# chrome_options = webdriver.ChromeOptions()
#
# browser = webdriver.Chrome(chrome_options=chrome_options)
#
# browser.set_window_size(1200, 850)
# wait = WebDriverWait(browser, 10)


def get_page():
	for t in range(200):
		url = "http://www.1kkk.com/image3.ashx?t=%s" % t
		with open('.\img\%s' % (str(t)+'.png'), 'wb') as f:
			response = requests.get(url)
			f.write(response.content)
			print(t)


def cut_png():
	png_list = os.listdir('./img')
	for i in png_list:
		img = Image.open('./img/%s' % i)
		cropng1 = img.crop((0, 0, 76, 76))
		cropng1.save('./cropimg/%s' % ('one' + i))
		cropng2 = img.crop((76, 0, 152, 76))
		cropng2.save('./cropimg/%s' % ('two' + i))
		cropng3 = img.crop((152, 0, 228, 76))
		cropng3.save('./cropimg/%s' % ('three' + i))
		cropng4 = img.crop((228, 0, 304, 76))
		cropng4.save('./cropimg/%s' % ('four' + i))
		print(i)


def differ():
	image1 = cv2.imread("./cropimg/four19.png")

	image2 = cv2.imread("./cropimg/four37.png")
	difference = cv2.subtract(image1, image2)
	result = not np.any(difference)  # if difference is all zeros it will return False

	if result is True:
		print("两张图片一样")
	else:
		cv2.imwrite("result.jpg", difference)
		print("两张图片不一样")


if __name__ == '__main__':
	differ()