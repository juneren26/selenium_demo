# coding=utf-8
'''
@Time   :2020/11/20 10:53
@Author :六月
@Email  :juneren26@gmail.com
@File   :assert_cart.py
@IDE    :PyCharm
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from exercise06.chrome_options import Options
# 设置浏览器
driver = webdriver.Chrome(options=Options().options_conf())
# driver.maximize_window()
driver.implicitly_wait(3)
# 获取iphone手机页面并切iframe登陆
driver.get('http://39.98.138.157/shopxo/index.php?s=/index/goods/index/id/2.html')
WebDriverWait(driver, 1, 0.5).until(lambda el: driver.find_element(By.XPATH, value='//*[@title="加入购物车"]'),
                                    message='元素未找到')
driver.find_element(By.XPATH, value='//*[@title="加入购物车"]').click()
iframe = driver.find_element_by_xpath('//*[@id="common-popup-modal-login"]/div/iframe')
driver.switch_to.frame(iframe)
driver.find_element(By.NAME, value='accounts').send_keys('supmahu_123')
driver.find_element(By.NAME, value='pwd').send_keys('supmahu_123')
driver.find_element(By.XPATH, value='//div[1]/form/div[4]/button').click()
driver.switch_to.default_content()
time.sleep(3)
# js修改手机属性可同时选择
js1 = "document.getElementsByClassName('sku-line  sku-line-images sku-dont-choose')[1].setAttribute('class','sku-line  sku-line-images')"
driver.execute_script(js1)
js2 = "document.getElementsByClassName('sku-line sku-dont-choose')[1].setAttribute('class','sku-line')"
driver.execute_script(js2)
time.sleep(3)
driver.find_element(By.XPATH, value='//*[@data-value="套餐一"]').click()
time.sleep(1)
driver.find_element(By.XPATH, value='//*[@data-value="金色"]').click()
time.sleep(1)
driver.find_element(By.XPATH, value='//*[@data-value="32G"]').click()
time.sleep(1)
driver.find_element(By.XPATH, value='//*[@title="加入购物车"]').click()
time.sleep(1)
# 切换到购物车页面校验是否加购成功
driver.find_element_by_xpath('//span[text()="购物车"]').click()
# product_cart = '苹果（Apple）iPhone 6 Plus (A1524)移动联通电信4G手机 金色 16G'
# el = driver.find_element_by_link_text('苹果（Apple）iPhone 6 Plus (A1524)移动联通电信4G手机 金色 16G').text
# assert product_cart == el, '添加购物车失败'
WebDriverWait(driver, 2, 0.5).until(
    lambda el: driver.find_element_by_link_text('苹果（Apple）iPhone 6 Plus (A1524)移动联通电信4G手机 金色 16G'), message='添加购物车失败')
