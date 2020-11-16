# coding=utf-8
'''
@Time   :2020/11/16 9:49
@Author :六月
@Email  :juneren26@gmail.com
@File   :shopxo01.py
@IDE    :PyCharm
'''
from selenium import webdriver
import time

# 注册操作
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://39.98.138.157/shopxo/index.php')
driver.find_element(by='link text', value='注册').click()
account = driver.find_element(by='xpath', value='//div[@data-am-widget="tabs"]/div/div/form/div/input')
account.send_keys('supmahu_123')
pwd = driver.find_element(by='xpath', value='/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[2]/div/input')
pwd.send_keys('supmahu_123')
driver.find_element(by='xpath', value='//div[4]/div/div/div/div[2]/div/div/div[1]/form/div[3]/label').click()
driver.find_element(by='xpath', value='//div[4]/div/div/div/div[2]/div/div/div[1]/form/div[4]/button').click()
time.sleep(1)
ex = driver.find_element(by='xpath', value='//p[text()="账号已存在"]')
print(ex)
# 判断账号是否存在，若存在则去登陆，若不存在则注册成功自动登陆三秒后退出
if ex != None:
    driver.find_element(by='xpath', value='//div[4]/div/div/div/div[1]/a').click()
    time.sleep(1)
    driver.find_element(by='xpath', value='//*[@placeholder="用户名/手机/邮箱"]').send_keys("supmahu_123")
    driver.find_element(by='xpath', value='//*[@placeholder="登录密码"]').send_keys('supmahu_123')
    driver.find_element(by='xpath', value='//div[4]/div/div[2]/div[2]/form/div[3]/button').click()
else:
    time.sleep(3)
time.sleep(3)
driver.close()
