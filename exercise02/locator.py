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
4.partial link text :和link text是一样的
5.classname
6.tagname :通过标签名来进行元素查找，一般用于定位下拉列表框的值，或者用于多个元素定位
7.cssselector :基于Class样式进行查找，有自己的固定表达式，类似于xpath，作为应用广度仅次于xpath
                
8.xpath :定位界的万金油
'''
