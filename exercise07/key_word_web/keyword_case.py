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


# 确定浏览器输入类型
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
    def open(self, **kwargs):
        self.driver.get(kwargs['txt'])

    # 关闭标签页
    def close(self, **kwargs):
        self.driver.close()

    # 退出浏览器
    def quit(self, **kwargs):
        self.driver.quit()

    # 定位
    def locator(self, **kwargs):
        try:
            self.driver.find_element(kwargs['name'], kwargs['value'])
        except Exception as e:
            print(e)
        return self.driver.find_element(kwargs['name'], kwargs['value'])

    # 输入
    def input(self, **kwargs):
        self.locator(**kwargs).send_keys(kwargs['txt'])

    # 点击
    def click(self, **kwargs):
        self.locator(**kwargs).click()

    # 断言
    def assert_text(self, fact_text, **kwargs):
        assert self.locator(**kwargs).text == fact_text

    # 强制等待
    def wait(self, **kwargs):
        sleep(kwargs['txt'])

    # 切换窗口
    def switchhandle(self):
        all_windows = self.driver.window_handles
        windows_cur = self.driver.current_window_handle
        for windows in all_windows:
            if windows != windows_cur:
                self.driver.switch_to.window(windows)

    # 切换iframe
    def switchframe(self, **kwargs):
        self.driver.switch_to.frame(self.locator(**kwargs))

    # 从iframe返回上层
    def reframe(self):
        self.driver.switch_to.default_content()

    # alert弹窗及confirm操作
    def alert_(self, name, value):
        web_alert = self.driver.switch_to.alert
        if name == '确定':
            web_alert.accept()
        elif name == '取消':
            web_alert.dismiss()
        elif name == '输入':
            web_alert.send_keys(value)
