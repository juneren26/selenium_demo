# coding=utf-8
'''
@Time   :2020/11/18 12:58
@Author :六月
@Email  :juneren26@gmail.com
@File   :shopxo_cart.py
@IDE    :PyCharm
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# 设置浏览器、最大化、隐式等待
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get('http://39.98.138.157/shopxo/index.php?s=/index/goods/index/id/2.html')
# 设置显示等待
WebDriverWait(driver, 1, 0.5).until(lambda el: driver.find_element(By.XPATH, value='//*[@title="加入购物车"]'),
                                    message='元素未加载完毕')
driver.find_element(By.XPATH, value='//*[@title="加入购物车"]').click()
iframe = driver.find_element(By.XPATH, value='//*[@id="common-popup-modal-login"]/div/iframe')
driver.switch_to.frame(iframe)
driver.find_element(By.NAME, value='accounts').send_keys('supmahu_123')
driver.find_element(By.NAME, value='pwd').send_keys('supmahu_123')
driver.find_element(By.XPATH, value='//div[1]/form/div[4]/button').click()
# 从iframe切换回上一级操作
driver.switch_to.default_content()
# 设置强制等待
time.sleep(2)
driver.find_element(By.XPATH, value='//*[@data-value="套餐一"]').click()
# WebDriverWait(driver, 1, 0.5).until(lambda el: driver.find_element(By.XPATH, value='//*[@data-value="金色"]'),
#                                     message='元素未加载完毕')
time.sleep(1)
driver.find_element(By.XPATH, value='//*[@data-value="金色"]').click()
# WebDriverWait(driver, 2, 0.5).until(lambda el: driver.find_element(By.XPATH, value='//*[@data-value="32G"]'),
#                                     message='元素未加载完毕')
time.sleep(1)
driver.find_element(By.XPATH, value='//*[@data-value="32G"]').click()
# WebDriverWait(driver, 2, 0.5).until(lambda el: driver.find_element(By.XPATH, value='//*[@title="加入购物车"]'),
#                                     message='元素未加载完毕')
time.sleep(1)
driver.find_element(By.XPATH, value='//*[@title="加入购物车"]').click()

driver.quit()
