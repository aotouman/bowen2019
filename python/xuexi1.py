#!/usr/bin/python
#-*- coding:utf-8 -*-


 #多变量赋值
# input
# a,c,b=3,8,'yy'
# #打印变量值
# print(b)
# #变量名的命名规则
# #3 数据类型
# #    python 的函数 type() 查看数据类型
# a='123'
# print(type(a))
# b=123.88
# print(type(b))
# #字符串   一串字符的集合
# #  不可变  支持索引  支持切片
# k='djfhuw234543'
# print(k[-3])
# #切片时只有1个数字和一个冒号，带有一个冒号：
# #冒号在前，默认从开始到结束
# #冒号在后，默认从开始到最后
# print(k[:5])
# print(k[6:])
# #切片时只有一个数字和两个冒号时
# #冒号在前，是以数字个数分组，每次去每一组的第一个
# #冒号在后，默认的从开始值到最后
# print(k[::2])
# print(k[3::])
# #切片时只有2个数字和两个冒号时
# #第一个数字代表每一组的下标值
# a='hefuxjoasi2354jshf'
# print(a[2::4])
# #属于字符串的函数
# #1，将所有的小写变大写  upper（）
# b=k.upper()
# print(b)
# #2替换，将字符串中的某些字符替换成其他字符
# b=a.replace('he','24')
# print(b)
# #4去除左右的空格  strip（） lstrip去除左边的空格 rstrip 去除右边的空格
# #去除中间的空格
# a='ew ertfr oi 34 ds'
# b=a.replace (' ','')
# print(b)
# #lstrip去除左边的空格
# #5.判断是否以某些字符串开头的
# k='djfhuw234543'
# b=k.startswith('jf')
# print(b)
# b=k.endswith('43')
# print(b)
# #连接，以某个字符为连接符，将列表变更成连接符
# b=k.split('23')
# print(b)
# c='+'.join(b)
# print(c)
# #join（）
# #格式化字符串
# #字符串不可变
# #填充字符串{}占位符    %字符占位
#
# #%s能填充任意字符%d只能填充数字
# #统计字符串中的某个字符个数  count（）
# len
# #列表 list 一组数据的集合
# a=[24,33,'jb','ss']
# print (type(a))









#a=[24,33,'jb','tt']
#print(type(a))
#增加，删除，改
#增加给列表添加数据每次只能添加一个数据
#a.append(10)
#a.insert(3,'jb')在第三个位置增加jb
#删除指定元素(若有重复默认删除第一个）
#a.remove('jb')
#删除指定位置上的元素
#a.pop(2)
#a=[24,33,'jb','tt']
#更改  重新赋值
#a[-2]=30
#a=[24,10,8,33,11]只能是同种数据类型要么是数据要么是字符串
#a.sort()字符串以首字母在ASCII码中的位置排序的
#反转
# a=[24,10,8,8,'jb','mm','kb']
#a.reverse()
#获取某元素的下标位置
# b=a.index(8)
#统计有多少个
# b=a.count(8)
#嵌套数据

#深复制，完全复制

#元组 一组数据的集合
# 一小括号为标识，元素与元素之间用逗号隔开
#特点：不可变，支持索引，支持切片
# a=(24,8,10,'jb','kk')
#获取某个元素下标位置
#b=a.index(10)
#统计某元素的个数
# b=a.count(8)
# #统计元素的所有个数
# print(len(a))

#列表
# q=[13,11,'hd','ow',33,'kl']
# q.append(10)
# q.insert(3,'tt')
# q.remove('ow')
# # q.pop(4)
# cc=[12,23,34,45,657,88]
# q=[13,11,'hd','ow',33,'kl',cc]
# # cc.sort()
# q.reverse()
#统计列表中个个数时要将值赋给f
# f=q.count(33)
#将-3的数改为”ww“
# q[-3]=('ww')
#将cc加入到q中？
# tt=q.copy()
# cc.append(666)
# q.append(777)
#
# a={'name':'小明','age':'24'}
# print(type(a))
#增加和更改
#删除 pop  删除某个价值对
# a.pop('age')
# 默认删除最后一个价值对
# a.popitem()
# a={'name':'小明','age':'24'}
#获取所有键
# b=a.keys()
#获取所有值
# b=a.values()
# 获取键值对
# # b=a.items()
# a={'name':'小明','age':'24','sex':'男'}
# b={'p':24,"jj":65}
# a.update(b)
# print(a)

#集合 set  一组数据的集合
#以大括号为标识,格式{数据，数据。。。。}
#特点：可变  不允许重复  无序  不支持索引和切片
# a={12,23,43,65,'kk','ji','gy',12}
#增加  每次只能添加一个数据,不能添加可变性数据
# a.add(('qwe',111))
#删除指定数据
# a.remove(12)
# 随机删除一个
# a.pop()
#更新
# a={12,23,43,65,'kk','ji','gy',12}
# b={22,43,67}
# # a.update(b)
# #并集|   交集&   差集-
# print(b-a)
# a='asdfwqiudi123'
# # b=a.upper()
# b=a.replace('qi','jj',4)
# print(b)

#更改数据类型
# a=[23,45,75,]
# a=float(45)
# print(a)
# print(type(a))
#
#


