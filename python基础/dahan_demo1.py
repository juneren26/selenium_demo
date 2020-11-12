# coding=utf-8
'''
@Time   :2020/11/12 10:55
@Author :六月
@Email  :juneren26@gmail.com
@File   :dahan_demo1.py
@IDE    :PyCharm
'''
# python的基本语法
# 注释
# 单行注释用#号，可直接在行前添加#号注释本行，也可选择本行Ctrl+/来注释
# 多行注释可通过三个单引号'''1''',或者三个双引号"""1"""
'''
多行注释
'''
"""
多行注释
"""

# 输出语句
# 1.打印字符串
# 打印一个字符串
print('你好')
# 打印多个字符串
print('你好', '世界')

# 2.打印整数
print(5)
print(5 + 6)

# 3.打印变量
# 3.1打印单行
variable1 = 'abcdefg'
print(variable1)

# 多行打印
variable2 = 'aaa' \
            'bbb' \
            'ccc'
print(variable2)

# 3.2多行打印
variable3 = '''aaa
bbb
ccc'''
print(variable3)

# print函数自带换行效果
print(variable1)
print(variable2)
# 3.3若不想换行，可在后面加上end=''
print(variable1, end='')
print(variable2)

# 3.4打印多个变量
# print(变量1，变量2)
print('打印多个参数变量：', variable1, variable2)

# 3.5其他变量的打印，占位符
# 占位符字符串类型用%s,数字整型用%d,浮点数用%.nf(n代表取几位小数)
wenhou = '早安'
print('老毛，%s' % wenhou)
wenhou1 = 12.5
print('老毛，%.2f' % wenhou1)

# 输入语句
score = int(input('请输入分数：'))
print('分数: %.2f' % score)

a = input('请输入电话号码:')
if a[0] == '1' and len(a) == 11:
    print(a)

else:
    print('请输入1开头的11位数')
