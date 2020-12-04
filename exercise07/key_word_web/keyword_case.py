# coding=utf-8
'''
@Time   :2020/11/27 10:08
@Author :六月
@Email  :juneren26@gmail.com
@File   :keyword_case.py
@IDE    :PyCharm
'''
from time import sleep

from selenium import webdriver


def browser(type_):
    try:
        driver = getattr(webdriver, type_)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver

def Options(self):
    options = webdriver.ChromeOptions()
    return options



# 定义工具类
class WebKeys:
    # 定义一个浏览器
    # driver = webdriver.Chrome()
    # 构造函数
    def __init__(self, type_):
        self.driver = browser(type_)
        self.driver.maximize_window()
        


    # 访问url
    def open(self, url):
        self.driver.get(url)

    # 关闭标签页
    def close(self):
        self.driver.close()

    # 定位
    def locator(self, name, value):
        try:
            self.driver.find_element(name, value)
        except Exception as e:
            print(e)
        return self.driver.find_element(name, value)

    # 输入
    def input(self, name, value, txt):
        self.locator(name, value).send_keys(txt)

    # 点击
    def click(self, name, value):
        self.locator(name, value).click()

    # 断言
    def assert_text(self, name, value, fact_text):
        assert self.locator(name, value).text == fact_text

    # 强制等待
    def wait(self, time_):
        sleep(time_)
