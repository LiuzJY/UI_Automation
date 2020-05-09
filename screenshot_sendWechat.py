# -*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from PIL import Image
from datetime import datetime, timedelta
import locale
import itchat


def login(dr):
    dr.maximize_window()
    dr.get("http://10.25.150.103:19095/d/Kz4-4g6Wk/guan-jian-zhi-biao-zhan-shi-tu?orgId=1&kiosk=tv&from=now-6h&to=now")

    dr.find_element(By.NAME, 'user').send_keys("migu")
    dr.find_element(By.NAME, 'password').send_keys("migu")
    dr.find_element(By.NAME, 'password').send_keys(Keys.ENTER)


def screenshot(dr):
    img = dr.find_element(By.CSS_SELECTOR, '.react-grid-layout')
    dr.save_screenshot("screenshot.png")

    left = img.location['x']
    top = img.location['y']
    right = img.location['x'] + img.size['width']
    bottom = img.location['y'] + img.size['height']

    im = Image.open('screenshot.png')
    im = im.crop((left, top, right, bottom))  # 对浏览器截图进行裁剪
    im.save('monitor.png')


def msg():
    now = datetime.now()
    late = now - timedelta(hours=0.5)

    locale.setlocale(locale.LC_CTYPE, 'chinese')    # 时间及日期以中文格式显示
    time_msg = late.strftime('%m月%d日 %H:%M' + '-' + now.strftime('%H:%M'))
    msg_txt = "客户端后台系统 "+time_msg+" 系统运行正常"
    return msg_txt


if __name__ == '__main__':
    # driver = webdriver.Chrome()
    # login(driver)
    # sleep(3)
    # screenshot(driver)
    # driver.quit()

    # print(datetime.now())

    msg = msg()
    print(msg)
    # itchat.auto_login(hotReload=True)
    # users = itchat.search_chatrooms
    # print(users)