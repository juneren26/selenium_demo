# coding=utf-8
'''
@Time   :2020/11/27 10:08
@Author :六月
@Email  :juneren26@gmail.com
@File   :test_case.py
@IDE    :PyCharm
'''
from exercise07.key_word_web.keyword_case import WebKeys

driver = WebKeys('Chrome')
driver.open('https://tx.fs.com/cn/index.php?main_page=login')
driver.input('id', 'email_address_login', 'scot.ren@feisu.com')
driver.input('id', 'password_login', 'renzhao95626')
driver.click('id', 'user_login')
driver.wait(10)
driver.close()
