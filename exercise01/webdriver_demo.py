# coding=utf-8
'''
@Time   :2020/11/11 12:03
@Author :六月
@Email  :juneren26@gmail.com
@File   :webdriver_demo.py
@IDE    :PyCharm
'''
# 导包webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep

# 选择浏览器
browser = WebDriver(executable_path="chromedriver")

# 访问URL
browser.execute('get', {'url': 'http://www.baidu.com'})

# 定位百度输入框并输入海贼王
el = browser.find_element(by="id", value='kw')
el._execute("sendKeysToElement", {'text': "一拳超人",
                                  'value': ''})
sleep(1)

# 定位并执行搜索
el1 = browser.find_element(by="id", value='su')
el1._execute("clickElement")
sleep(1)

# 打印title并退出浏览器
print(browser.execute("getTitle"))
browser.service.stop()
