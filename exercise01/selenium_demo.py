# coding=utf-8
'''
@Time   :2020/11/11 10:03
@Author :六月
@Email  :juneren26@gmail.com
@File   :selenium_demo.py
@IDE    :PyCharm
'''
# 导入selenium.webdriver包
from selenium import webdriver
from time import sleep

# 选择浏览器
driver = webdriver.Chrome()

# 访问url
driver.get('http://www.baidu.com')

# 定位百度输入框并输入海贼王
input_ = driver.find_element_by_id('kw')
input_.send_keys('海贼王')
sleep(1)

# 定位、执行搜索操作
search = driver.find_element_by_id('su')
search.click()
sleep(1)

# 打印title、退出浏览器
print(driver.title)
driver.quit()
