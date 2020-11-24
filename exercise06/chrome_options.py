# coding=utf-8
'''
@Time   :2020/11/24 10:34
@Author :六月
@Email  :juneren26@gmail.com
@File   :chrome_options.py
@IDE    :PyCharm
'''

'''
配置ChromeOptions：一般作为一个专门的配置类进行存放
特殊场景下的浏览器配置需要自行查找资料添加，查找资料需注意代码版本
    新版本：driver = webdriver. Chrome(options=options)
    老版本：driver = webdriver.Chrome(chrome_options=options)
    因为老版本的options配置，配置参数是chrome_options,而新版本的参数时options
常用的浏览器配置项：
    1.去掉黄条警告
    2.窗体最大化
    3.读取本地缓存
    4.无头模式
    5.禁用密码管理窗体
'''
from selenium import webdriver


class Options:
    def options_conf(self):
        # 创建options对象：配置浏览器的设置
        options = webdriver.ChromeOptions()
        # 去掉默认的自动化提示：不去掉一般不会有任何影响，但在特殊情况下，黄条可能会遮挡到页面的内容
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 老版本的去掉提示
        # options.add_argument('disable-infobars')
        # 窗体最大化
        options.add_argument('start-maximized')
        # 加载本地缓存，让浏览器变成一个有缓存的模式
        '''
            1.通过指令查找本地的浏览器缓存，chrome://version
            2.通过传入本地缓存，来实现缓存的获取；参数 --user-data-dir=
            3.在调用本地缓存的时候，要先关闭所有正在应用的浏览器窗体
            4.因为需要加载本地缓存，所以在启动浏览器之后，运行脚本的第一条指令，速度会非常慢，
            如果想要提速，可以手动输入任意一个url访问，就可以提速了
            5.一般不推荐使用，如果非要绕过登陆来实现后续的操作行为，则再添加
            6.最廉价的验证码机制处理手段，仅限登陆部分
        '''
        # options.add_argument(r'--user-data-dir=C:\Users\Administrator\AppData\Local\Google\Chrome\User Data')
        # 添加配置去掉密码管理弹窗
        prefs = {}
        prefs['credentials_enable_service'] = False
        prefs['profile.password_manager_enable'] = False
        options.add_experimental_option('prefs', prefs)
        # 无头模式：Headless模式，无界面运行，会尽可能的降低GPU的使用率，整体及其的资源使用率会下降
        # options.add_argument('--headless')
        # 隐身模式：
        options.add_argument('incognito')
        # 指定窗口大小：目前好像不支持
        options.add_argument('-windows-size=720,1080')
        return options

if __name__ == '__main__':
    # 生成浏览器配置
    options = Options().options_conf()
    # 配置webdriver
    driver = webdriver.Chrome(options=options)

