# coding=utf-8
'''
@Time   :2020/11/12 22:31
@Author :六月
@Email  :juneren26@gmail.com
@File   :music163.py
'''
# 导入selenium.webdriver包
from selenium import webdriver
from time import sleep

# 选择浏览器设置等待
browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.maximize_window()
# 12点了访问网抑云获取当前窗口句柄
browser.get('http://music.163.com')
main_windows = browser.current_window_handle

# 查找登录元素点击
browser.find_element_by_xpath('//a[@data-action="login"]').click()

# 选择其他模式登录
browser.find_element_by_xpath('//*[@data-action="switch"]').click()

# 同意隐私条款&选择QQ登录
browser.find_element_by_xpath('//*[@type="checkbox"]').click()
browser.find_element_by_xpath('//div[@class="u-alt"]/ul/li[2]/a').click()
print(browser.title)

# 获取当前所有窗口句柄
all_windows = browser.window_handles

# 切换至qq登录窗口
for handle in all_windows:
    if handle != main_windows:
        browser.switch_to.window(handle)
qq_login_windows = browser.current_window_handle
sleep(5)
print(browser.title)

# 切换iframe
iframe = browser.find_element_by_xpath('//*[@id="ptlogin_iframe"]')
browser.switch_to.frame(iframe)
browser.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# 从iframe操作完后需要返回上一步操作  driver.switch_to.default_content()

# 输入账号密码登录
browser.find_element_by_xpath('//input[@id="u"]').send_keys(1339407609)  # 使用个人QQ账号
browser.find_element_by_xpath('//input[@id="p"]').send_keys('xxxxxxxxxx')  # 使用个人QQ密码
browser.find_element_by_xpath('//*[@id="login_button"]').click()

# 退出浏览器
browser.quit()