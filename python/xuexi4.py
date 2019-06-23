#!/usr/bin/python
#-*- coding:utf-8 -*-



#创建客户端
# import socket
# # 创建一个套接字
# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #连接服务器
#
# sock.connect(('192.168.0.62',3000))
# #将qq当做请求发送给服务器
# while True:
#    qq = input('>>>')
#    sock.send(qq.encode('utf-8'))
# #接受响应
#    ww = sock.recv(1024)
#    print(ww.decode('utf-8'))
   # sock.close()    #断开连接

# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# host = ('192.168.0.27',3000)
# while True:
#
#      msg = input('>>>')
#      s.sendto(msg.encode('utf-8'),host)
# #接受响应
#      reg = s.recv(1024)
#      print(reg.decode('utf-8'))





#正则表达式
# with open('a.txt','r')  as f:
#     a =f.read()
#匹配a中的数子
#自己写的正则表达式对于python来说python不认识
#需要将正则表达式转化为python=能够认识的语句

#贪婪模式：尽可能多的去匹配符合条件内容
# 非贪婪模式：尽可能少的去匹配符合条件的内容 (在匹配时加？)
#
# import  re
#将字符串转换成正则表达式
# a = ['q56wed','j213dvj435g56dh','435djhjh','gjhsdh435' ]
# with  open('c.txt','r') as  ff:
#     a = ff.read()
#     print(a)
#将正则表达式编译成python能够识别的正则语言
    # ff = a.compile('小(.*)24',re.S)
#拿着编译之后的正则到字符串中去查找
#查找所有符合条件的字符，结果是一个列表
# c = re.findall('213(.*)435',a,re.S)
#替换 :将字符串中的某些字符替换为其他
# for  i in a:
#     #第一个参数：通过正则过滤出被替换的字符
#     #第二个参数：替换成的字符
#     #第三个参数：要被替换的字符串
#      c = re.sub('[0-9]+','abc',i)
# print(ff)

#面向对象
#将函数进行分类和封装，使开发更高效

# from  xixi.py  import *
#1定义一个类    class   类名：
# 属性，方法（函数）
#2 调用  类名（）.函数名（）
#3  继承
# class  Cj():
#     def  pp(self):
#         print('iloveyou')
# #self  不是函数的参数 ，self是类的实例，方便在类的内部调用其他函数
#         self.oo()    #self相当于self=Cj()
#     def oo(self):
#         print('don  you  love')
# class  Cc():
#     def xn(self):
#         print('whant to you')
#         self.hh()
#     def hh(self):
#         print('marry me')
# # #3括号中写要继承的类
# # #3新的类会继承旧的类中的所有函数
#
# class qwe():
#     def yy(self0):
#         print('kill')
# class  asd(qwe,Cj,Cc):     #括号中跟得是类名
#     pass
# q = asd()     #将类赋值给变量
# q.oo()        #调用
# q.pp()
# q.yy()

# 类的实例（对象）
# 将类名()赋值给了一个对象
# sh=Cj()
# qq=Cc()
# sh叫 类的实例（对象）
# sh.pp()
# qq.xn()

#4多态(方法重写)
#继承的类中某个函数不满足需求的
#本类中自定义一个跟继承的类中函数名相同的函数

# from xixi  import Cj
# class  asd(Cj):
#     def uu(self):
#         print(999)
#         self.__oo()
#     def __oo(self):
#         print(666)
#         print('hello')
# q = asd()
# q.()
#5.私有方法（函数）
#不可被继承的，不能在类的外部调用的
#在函数名的左边加两个下滑线  只能在内部调用(保留隐秘性）
#6.类的专有方法
# 函数名左右两边都有两个下滑线,是python内部固定的
#只要是个类,就具有所有的专有方法
#专有方法是不需要调用会自动执行的
#属性:一个类中的所有函数都具有的特点      就是基础值
#定义属性   在类下面  变量名="zhi"
# from xixi  import Cj
# class  asd(Cj):
#     def __init__(self):   #初始化属性
#         self.a=4
#         self.b=8
# q = asd()
# class wangzhe():
#     #定义属性
#     # name='亚瑟'
#     # xueliang=1000
#     def __init__(self,name,xueliang,kaida):   #初始化属性
#         self.name=name
#         self.xueliang=xueliang
#         self.kaida=kaida
#     def tuita(self,x,y):
#
#         self.xueliang  -= 400
#         print('{},还剩下{}{}{}'.format(self.name,self.xueliang,x,y))
#     def jiaxue(self,x):
#         self.xueliang += 600
#         print('{},还剩下{}'.format(self.name,self.xueliang))
#     def jineng(self,y):
#         self.kaida  +=  ''
#         print('{}技能{}{}'.format(self.name,self.kaida,y))
# q = wangzhe('妲己',1200,'降龙十八掌')
# w = wangzhe('后羿',1100,'降龙十八掌')
# q.tuita('九阳','是')
# q.jineng('乾坤大挪移')

#面像对象:优点;可扩展,易维护,可重复使用y
#面向过程:优点;性能好;缺点:不易维护,不可重复使用
#面向对象:通过代码和逻辑一步一步实现要达到的目的

#爬虫：模仿浏览器，根据自己制定的规则批量下载指定的资源
#分类：聚焦爬虫，搜索爬虫
#聚焦爬虫：只针对某个网站进行爬虫
#搜索爬虫：争对全网络进行爬取(搜索引擎)
#可以模仿浏览器的模块：request(第三方模块需要下载)，urllib,urllib2,urllib3
#过滤网页资源：re(正则表达式)，BeautSoup，xpath

#爬虫第一步:分析网址
#爬虫第二不;找到想要的资源并过滤

#对服务器进行请求，将得到的响应数据过滤并保存
#由于会给服务器带来极大的压力，所以开发人员由一个反爬；为了防止爬虫批量下载数据
# 1,通过请求 headers判断    将字段中加入os版本号，添加的多的越私密
# 2，IP地址被封  频繁的转换公网IP（西刺代理）
# 3，验证码
# 4，数据混淆  5，行为分析
#爬虫本身不违法，做商业活动就犯法

#
# import requests
# import re

# class  FreeBuf():
#
#     def send_请求(self,page):
#         url = 'https://www.freebuf.com/page/{}'.format(page)   #page/{}'.forment(page)
# #         #发送请求
#         head = {
#               'User-Agent': 'Mozilla/5.0 (WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/70.0.3538.110Safari/537.36'
#           }    #添加上你的客服端的主机版本号h
#
#         res = requests.post(url,headers=head)
# #         #读取结果1.text以文本的形式接受,结果是一个字符串
#         # print(res.text)
#         #       2，content以字节方式接收
#         hh=res.content.decode('utf-8')
#         return hh
#     def guolv(self,x):
#         #二次过滤
#         title=[]
#         patt = re.compile('<div class="news-info">(.*?)<dd>',re.S)
#         itesms = patt.findall(x)
#         for i  in itesms:
#             aa = re.findall('title="(.*?)"',i)
#             title.append(aa[0])
#         return title
#     def save(self,y):
#         with  open('a.txt','a',encoding='utf-8') as f:
#             for i in y:
#                 f.write(i+'\n')
#
# fr = FreeBuf()
# for i in range(1,5):
#    hh=fr.send_请求(i)
#    fr.guolv(hh)
#    tt=fr.guolv(hh)
#    fr.save(tt)

# url = 'https://www.qiushibaike.com/imgrank/page/2'
# head = {'User-Agent': 'Mozilla/5.0 (WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/70.0.3538.110Safari/537.36'
#         }
# res = requests.get(url,headers=head)
# html = res.content.decode('utf-8')
#
# #过滤
# patt = re.compile(r'<img src="//pic.qiushibaike.com/system/pictures/(.*?).jpg"')
# patt1 = re.compile(r'<img src="//static.qiushibaike.com/images/(.*?).png')  另一种和格式的图片
# items = patt.findall(html)
# items1 = patt1.findall(html)
# print(len(items1))
# print(len(items))     打印出图片的个数
# a = 0
# for i in items:
#     j ='http://pic.qiushibaike.com/system/pictures/'+i+'.jpg'
#     #保存图片     先对图片链接请求，以字节的方式读取，
#     msg = requests.get(j,headers=head)
#     hh = msg.content
#     with open('{}.jpg'.format(a),'wb')  as f:
#         f.write(hh)
#     a += 1

# 豆瓣网
# import requests
# import re
# url = 'https://movie.douban.com/top250'
# head = {'User-Agent': 'Mozilla/5.0 (WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/70.0.3538.110Safari/537.36'
#         }
# res = requests.get(url,headers=head)
# html = res.content.decode('utf-8')
# a = []
# patt = re.compile(r'<img width="100" alt="(.*?)"' )
# items = patt.findall(html)
# a.extend(items)
#
# pa= re.compile(r'src="https://img(.).doubanio.com/view/photo/s_ratio_poster/public/(.*?).jpg" class="">')
# it1 = pa.findall(html)
# b = 0
# for i in it1:
#     j = r'http://img{}.doubanio.com/view/photo/s_ratio_poster/public/{}.jpg'.format(i[0],i[1])
#     msg = requests.get(j,headers=head)
#     hh = msg.content
#     with open(r'C:\Users\xiaoxiannv\Desktop\tupian\{}.jpg'.format(a[b]),'wb') as f:
#         f.write(hh)
#     b += 1
# 删除多
# import os
# a = os.getcwd()
# aa = os.listdir(a)
# for i in aa:
#     c = str(i)
#     d = c.endswith('.jpg')
#     if d == True:
#         os.remove(i)


#网页     静态网页，所有的资源都在html文件上
#        动态网页. 资源不在html文件上（自己手动输入查找）
#ajax(XHR就是它的报文)   JavaScript(js是他的报文
# 网页原代嘛叫json ：是一种轻量级的数据传输格式：
# import json  是可以把字符串变成字典，将内容解读为python能够识别的语言
# import json
# import requests
# url = ''
# res = requests.get(url)
# h = res.content.decode('utf-8')
# #将字符串转换成字典
# pp = json.load(h)
# print('加上路径，已字典的键名就可以一级一级的查找')  #也可以写成循环语句查找
# #将字典转换成json字符串
# uu= json.dumps(pp)
# print(type(uu))

#zip()将多个列表一一对应
# a = [12,34,123,53]      #查找出来的链接
# b = ['a','b','c','d']   #名称
# c = [122,24]
# aa = zip(b,a,c)   #将多个列表一一对应  以少的数据优先
# print(list(aa))
# print(dict(aa))




























