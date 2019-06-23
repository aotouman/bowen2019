#!/usr/bin/python
#-*-coding:utf-8 -*-
#判断语句
#单分支判断
#格式：  if 条件：  执行语句
#跟shell的区别：不需要then,fi  执行语句必须要有缩进   条件后面必须要有冒号
#
# a=input()
# a=int(a)
# if   a >  4:
#     print('hell')
#双分支语句
#格式  if 条件: 执行语句  else  条件：  执行语句
#
# 多分支语句
# a=8
# if  a>6:
#     print('zs')
# elif a<10:
#     print('jd')
# elif  a==8:
#     print('kb')
#打印出成绩表
# a=input('>>>')
# a=int(a)
# if   a>=90:
#     print('优')
# elif   90> a >=80:
#     print('良')
# elif   80>  a >=70:
#     print('及格')
#嵌套判断  判断语句中写入判断语句
# a=9
# if  a%2==0:
#     if a%3==0:
#         print('hello')
#     else:
#         print('24')

#手动打印一个数字
#1既能除以2又能厨艺3打印hello  world
#2只能除以2不能除以3打印hello
#3不能除以2能除以3打印world
#4都不能除答应23
# a=input('>>>')
# a=int(a)
# if a%2==0:
#     if a%3==0:
#         print('hello  world')
#     else:
#         print('hello')
# elif a%3==0:
#     print('world')
# else:
#     print('123')
#循环语句  for  while
#格式  for  变量名  in 范围：  执行语句
#range  可以将数字变更成一个范围
# a= [12,24,23]
# for  i in a:
#     print(i)
# a=5
# for  i  in range(a):
#     print(i)
#递进数（range)
# for  i  in range(1,100,34):
#     print(i)
#从一加到一百
# a=101
# sum=0
# for i in range(a):
#    sum=sum+i
# print( sm=0
# sum=0
# for x in range(1,100,2):
#   sum=sum+x
# print(sum)
# snm=0
# for y in range(2,100,2):
#   snm=snm+y
# print(snm)
# sm=sum-snm
# print(sm)

#循环嵌套   for语句加入if
  #        for语句加入for
# for  i  in range(10):
#     if i > 5:
#         print('0')
#     else:
#         print('24')

#循环嵌套
#break  continue
# 7不打印
#  for i in range(10):
#    if  i==7:
#        continue
#      print(i)
# for i in range(10):
#     if i >7:
#         break
#     print(i)
#
# import  random
# a = random.randrange(1,10)
# for x in range(4):
#     b=input('>>>')
#     b=int(b)
#     if b == a:
#         print('答对了')
#         break
#     elif b > a:
#         print('大了')
#     else:
#         print('小了')

#  for......else  语句
# import  random
# # a = random.randrange(1,10)
# # for x in range(3):
# #     b=input('>>>')
# #     b=int(b)
# #     if a == b:
# #         print('答对了')
# #         break
# #     elif a > b:
# #         print('大了')
# #     else:
# #         print('小了')
# # else:
# #     print('菜鸡')

# a=[12,24,34]
# for i in enumerate(a):取下标位置和值
#    print(i)
#九九乘法表
# for x in range(1,10,1):
#      for y in range(1,x+1):
#          print("{}*{}={}".format(x,y,x*y),end='\t')
#      if  y == x:
#              print("{}*{}={}".format(x, y, x * y))

# for x in range(1,10,1):
#      for y in range(1,x+1):
#          print("{}*{}={}".format(x,y,x*y),end='\t')
#      if  y == x:
#              print()


#100以内的质数之和
# sum=0
# for  i  in range(2,101,1):
#      for  j  in range(2,101,1):
#          x=i%j
#          if  x==0:
#              break
#      if j == i:
#       sum=sum+i
# print(sum)
# 1000以内的水仙花数
# for i in range(100,1000):
#     x=i//100
#     y=i%100//10
#     z=i%10
#     if x**3+y**3+z**3==i:
#        print(i)

#排序法
# sum=0
# for i in range(2,101,1):
#     for j in range(2,101,1):
#         a=i%j
#         if  a==0:
#             break
#     if  i==j:
#             sum=sum+i
# print(sum)
#回文字符串
# a=input('>>>')
# a=str(a)
# if  a==a[::-1]:此处不能用反转，因为这是一个字符串，而反转用于列表
#     print('回文字符串')
# else:
#     print('不是回文字符串')
# while循环    格式：while 条件：执行语句
#  根据是否符合条件来决定是否循环
#
# a=3
# # while  a>2:
# #     print('hello')
# #     a-=2 限制循环的次数

# sum=0
# a=1
# while  a <= 100:
#     a=a+1
#     sum=sum+a
# print(sum)

# while  True:  # 做为一个循环条件，目的使下面的循环进行
#     a=input('>>>')
#     a=a.split(',')  #以逗号分隔
#     for  i,j in enumerate(a):   #将一个列表变成整数
#         a[i]=int(j)
#     b=sum(a)//len(a)
#     if  a[1] < 0:     #若输入的式个负数就停止
#         break
#     print('平均数为{}'.format(b))
#     for  k  in  a:
#         if k  <  b:
#             print('低于平均数的有{}'.format(k))

#列表推导式
# while  True:
#     a=input('>>>')
#     a=a.split(',')
#     a=[int(i)  for i  in a]
#     b=sum(a)/len(a)
#     if  a[0] < 0:
#         break
#     print('平均数{}'.format(b))
#     c=[k  for k in a   if  k  < b]
#     print(c)

# a = [12,24,24,34,32,43,23,23,12]
# for i  in a:
#     b = a.count(i)
#     if  b > 1:
#         for  j  in   range(b-1):
#             a.remove(i)
# print(a)
# a = [12,24,24,34,32,43,23,23,12]
# b = []
# for  i in a:
#     b=a.append(i)
# print(b)

#对文件的操作
# f=open('c:\user\join\desktop\a.txt','w',encoding='utf-8')错误的因为斜杠需要转移
# f=open('c:\\user\\join\\desktop\a.txt','w',encoding='utf-8')
##向入数据文件里加#关闭文件
# f= open(r'b.txt','a',encoding='utf-8')
# for   i  in  range(10):
#    f.write('dfewgvcvg\n')只能写入一个字符串，write本身就式不换行
#    f.write('123')
# f.close()
# kk= open(r'c.txt','w',encoding='utf-8')
# for  i  in  range(1,10,1):
#     for  j in range(1,i+1):
#         kk.write('{}*{}={}\t'.format(i,j,i*j))
#     kk.write('\n')
# kk.close()
# kk= open(r'c.txt','r',encoding='utf-8')
# # b=kk.read()  #读取文件中的内容，结果是个字符串
# # b=kk.readlines()
# b=kk.readline()
# c=kk.readline()
# print(c,b)
# kk.close()

# q=open(r'c.txt','r',encoding='utf-8')
# a=q.readlines()
# for i  in  a:
#     if  i[:3]=='abc':
#        print(i)
# q.close()
# q=open(r'c.txt','r',encoding='utf-8')
# for i in  range(5,10):
#   if  i  >=  5:
#      q.readline(i)
#      print(q.readline(i))
# q.close()
# q=open(r'c.txt','r',encoding='utf-8')
# b=q.readline()
# c=str(b)
# for  a  in  c:
#     if  a==c.startswith('abc'):
#        print(a)
#判断三角形
# a = input('>>>')
# a = int(a)
# b = input('>>>')
# b = int(b)
# c = input('>>>')
# c = int(c)
# if  a+b>c  and a+c>b  and  b+c>a:
#     print(a,b,c)
#     print('是三角形')
# 判断以什么开头以什么结尾
#
#
# f = open('af.jpeg','rb')
# b=f.read()
# print(b)
# # f.close()
# x = open('tt.jpeg','wb')
# x.write(b)
# x.close()

#with  语句  上下文管理器
# 格式  with  要操作的对象  as  变量：  执行语句
#自动释放占用空间，到后会自动关闭文件
#
# with open('b.txt','r+',encoding='utf-8')  as f:
#     b = f.read()
#     f.write('fadjh')
# print(b)

#函数  可重复使用的具有某种功能的代码块
#格式：  def   函数名（）； 语句块
#调用函数  函数名（）
# def   a():
#     b=0
#     for  i  in range(1,101):
#         b+=i
#     print(b)


#5.	判断以什么开头，以什么结束

# b = open('c.txt','r',encoding='utf-8')
# for  x  in  range(15):
#   x = b.readline()
#   c = x.startswith('abc')
#   c = x.endswith('j')
#   if  True==c :
#      print(x)


#选择排序
# a = input('>>>')
# a = a.split(',')
# a = [int(c) for c in  a]
# for  i  in  range(len(a)):
#     for  j in  range(len(a)-1):
#         if  a[i] < a[j]:
#            t=a[i]
#            a[i]=a[j]
#            a[j]=t
# print(a)
#三次猜数字
#import random
# # a = random.randrange(1,10)
# # for i in range(3):
# #     b = input(">>>")
# #     b = int(b)
# #     if  b==a:
# #          print('恭喜答对')
# #          break
# #     elif b>a:
# #          print('大了')
# #     elif b<a:
# #          print('小了')
#水仙花数
# for  i  in  range(100,1001,1):
#     a=i//100
#     b=i%100//10
#     c=i%10
#     if a**3+b**3+c**3==i:
#        print(i)
#打印所有大一大和第二大的数
# a = input('>>>')
# a = a.split(',')
# a = [int(c) for c in a]
# for i in  range(len(a)):
#     for  j  in  range(len(a)-1):
#         if  a[i] < a[j]:
#             t=a[i]
#             a[i]=a[j]
#             a[j]=t
# print(a[-2:])

#变量的作用域
#局部变量   全局变量
# b=1            #全局变量
# def a():
#     global  b   #将局部变量变更成全局变量
#     b=0         #局部变量
#     print(b)
# a()
# print(b)
#3.传参
# 定义函数   def  函数名（参数名）：执行语句
#参数可以有任意多个，必须参数：使用函数时必须得传入参数
#默认参数：使用函数时可以传入

# def  tt(b=100):
#     a=0
#     for  i in range(b+1):
#        a=a+i
#     print(a)
#
# tt()
#质数之和  传参得方式：
# def z(x):
#     sum=0
#     for i in range(2,x+1):
#         for  j in range(2,i):
#             a=i%j
#             if  a==0:
#                break
#         else:
#             sum=sum+i
#     print(sum)
# z(100)
# def asd(a,b=10,*args):    #将数据放在了一个元组中
#     print(b,*args)
# asd(100)

#4.return  结束函数和赋值
# def  asd(b=10):
#     a=0
#     for  i  in   range(1,b):
#         a += i
#     print(a)
#     return  a
# x=asd()
# print(x)

# def  q(x):
#     a=0
#     for i  in range(1,x+1):
#         a  += i
#     return a
# for j in range(10,41,10):
#     c=q(j)+2
#     print(c)


#加减乘除
# def math(x,y,z):
#     if z=="+":
#         c=x+y
#     if z=="-":
#         c=x-y
#     if z=="*":
#         c=x*y
#     if z=="/":
#         c=x/y
#     return c
# b=math(3,4,'*')
# print(b)
#lambda  匿名函数
# a=lambda x,y: x+y
# b=lambda x,y: x-y
# c=lambda x,y: x*y
# e=lambda x,y: x/y
# while   True:
#     s=input('>>>')
#     if '-'  in  s:
#         d = s.split('-')
#         print(b(int(d[0]),int(d[1])))
#     elif '+' in s:
#         d = s.split('+')
#         print(a(int(d[0]), int(d[1])))
#     elif '*'  in  s:
#         d = s.split('*')
#         print(c(int(d[0]),int(d[1])))
#     elif '/'  in  s:
#         d = s.split('/')
#         print(e(int(d[0]),int(d[1])))
#     else:
#         break


# def  wc(x,y,z):
#     x=list(x)
#     d=y+z
#     if  d > len(x):
#         d=len(x)
#     for  i in range(y,d):
#         x.pop(y)
#     b=''.join(x)
#     print(b)
# wc('hdjfehhjdcf',2,12)

#输入四个数随机组成三位数不重复
# b=input('>>>')
# b=b.split(',')
# b=[int(x) for x in b]
# for  i  in range(len(b)):
#     for  j  in range(len(b)):
#           for  m  in range(len(b)):
#             if b[i]!=b[j] and b[j] != b[m] and b[i] != b[m]:
#                 c = 100*b[i]+10*b[j]+1*b[m]
#                 print(c)

# def  lift(x,y):
#     for i in range(y%len(x)):
#         x.insert(0,x.pop())
#         return x
# x=[1,2,3,4,5,6]
# a=lift(x,2b)

#将十进制转化成十六进制
# a = int(input('>>'))
# ff = [str(i)  for i  in  range(10)]+['a','b','c','d','e','f']
# c = ''
# while  True:
#     b = a%16
#     c = c+ff[b]
#     a = a//16
#     if a==0:
#         break
# print(c[::-1])

#导入语句
# # import 语句    import + 文件名
# def  asd():
#     print('hello')
#
#   #    from  文件名  import  函数名
# def  po():
#     print('tt')
# po()
# #判断正在执行的文件，是否是本文件
# if __name__ == '__main__':
#     for  i in range(10):
#         print(i)






