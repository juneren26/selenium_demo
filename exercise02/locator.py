# coding=utf-8
'''
@Time   :2020/11/12 20:47
@Author :六月
@Email  :juneren26@gmail.com
@File   :locator.py
'''

# 八大元素定位

from selenium import webdriver

'''
1.id :类似于身份证的身份证号码，但为了避免出现重复，最好在定位之前校验一下
2.name :类似于身份证的名字，容易重名
3.link text :一般用于定位a标签这一类超链接，通过text定位
4.partial link text :和link text是一样的。不同于这是模糊查询，类似于sql中的like关键字
5.classname :通过class属性进行元素查找，除非无奈否则不要使用它（元素定位一定不会到无奈的地步）
6.tagname :通过标签名来进行元素查找，一般用于定位下拉列表框的值，或者用于多个元素定位，向后台系统新增后，下拉列表至变动
7.cssselector :基于Class样式进行查找，有自己的固定表达式，类似于xpath，作为应用广度仅次于xpath
    一般直接使用xpath即可，只有在出现伪元素（after before ......）会应用这个定位方法
8.xpath :定位界的万金油
    xpath定为形式类似于文件系统，根据路径来查找元素
    相对路径 ： //*[@id="kw"]   //*[text()="登陆"]
        // 根路径
        * 所有元素
        [] 筛选条件
        @ 通过属性定位
        text() 通过text文本筛选
        " " 要查找的值
    绝对路径 ： /html/body/div/div[2]/div[5]/div[1]/div/form/span[1]/input 不可取，一般不用这种方式进行定位
    xpath的定位不推荐使用class属性进行定位
    xpath的函数：
        contains ： 通过模糊查找来查找元素属性或文本，继而查找到这个元素
        //*[contains(@id,'search')]
        //*[contains(text(),'search')]
'''

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# 通过id查找元素
# driver.find_element_by_id('kw')
# 通过name查找元素
# driver.find_element_by_name('wd')
# 通过link text查找元素
# driver.find_element_by_link_text('新闻')
# 通过partial link text定位
driver.find_element_by_partial_link_text('新')
# 通过classname定位
# driver.find_element_by_class_name("s_ipt")
# 通过tagname定位
# list1 = driver.find_elements_by_tag_name('a')  # elements 用于查找多个元素，结果会返回一个list
# list1 = driver.find_element_by_tag_name('a') #定位的是第一个a标签元素
#cssselector定位
# driver.find_element_by_css_selector('#kw')
#xpath元素定位
# driver.find_element_by_xpath('//*[@id="kw"]')

driver.quit()

