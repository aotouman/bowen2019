#调用asd()  函数
#  xuexi2中的代码导入到day2中

# import xuexi2      #没有后缀,
# #    #文件名加函数
# xuexi2.asd()
#  from 文件名  import  函数名      调用函数从文件中
# 调用  函数名
# from  xuexi2  import *
# import random

#异常处理
#语句  try   执行语句     except   执行语句
#如果try下面得语句报错，就执行except下面的语句
# try        except     else  语句
# 只要try 下面的语句正常执行就执行else语句
# try      except   finally
# 无论如何都会执行，不会受前面的影响
# try:
#     a=  123  + 689
#     c=  a  +  'ppo'
#     print(c)
# except   Exception  as e:  #默认后面能跟所有的错误
#     print(e)
# else:
#     print('jjyy')
# finally:
#     print('bb098')


# #xlwt是对excel表格进行写入数据模块
# import xlwt
# # #创建一个空的表
# f  = xlwt.Workbook(encoding='utf-8')
# # #添加一个标签页括号内是标签名
# sheet  = f.add_sheet('python_test')
# # #写入数据，第一个数字代表行，第二个数字代表列，第三个数字代表写入到内容
# for  i  in  range(1,10):
#     for  j in range(1,i+1):
        # sheet.write(i-1,j-1,'{}*{}={}'.format(i,j,i*j))
# #保存文件
# f.save('yy.xls')
# #读取excel表格的内容
# import  xlrd
# f = xlrd.open_workbook('yy.xls')
# #获取多少个标签页
# # b = f.nsheets
# # print(b)
# # #获取要读取得标签页，根据索引来获取
# # sheet = f.sheets()[0]
# #根据标签页的名称获取标签页
# # b = f.sheet_names()
# # print(b)
# #获取标签的名称
# sheet = f.sheet_by_name('python_test')
# # #获取文件中有多少行
# # b = sheet.nrows
# # #读取某一行的内容
# # for  i  in range(b):
# #     c=sheet.row_values(i)
# #     print(b)
# # 获取多少列
# # b = sheet.ncols
# # print(b)
# # #读取某一列的数据
# # c = sheet.col_values(0)
# # print(c)
# # 读取某个单元格的内容
# b = sheet.cell(6,10).value
# print(b)
#

# import xlwt
# import  xlrd
# from  xlutils.copy  import copy
#
# with open('cj.txt', 'r', encoding='utf-8') as f:
#     c = []
#     b = f.readlines()
#     for i in b:
#         i = i.split(',')
#         c.append(i)
#
# kk = xlwt.Workbook(encoding='utf-8')
# sheet = kk.add_sheet('sheet1')
# for  j  in range(len(c)):
#     for  y in range(len(i)):
#         sheet.write(j,y,'{}'.format(c[j][y]))
# kk.save('yy.xls')




#给excel表格中追加内容
# from  xlutils.copy  import copy
# import  xlrd
# #打开要追加的文件
# f = xlrd.open_workbook('yy.xls')
# sheet1 = f.shtte2()[0]
# b = sheet1.nrows
# #复制文件
# new_f = copy(f)
# #获取要追加的标签页,通过索引
# sheet = new_f.get_sheet(0)
# #写入
# sheet.write(0,2,'jj')
# #保存
# new_f.save('tt.xls')

#时间模块（自带模块）
# import time
#时间戳:从公元1970年
# a = time.time()
#以元组的格式默认显示的时间  是否是夏令时/冬令时
#可以传入参数的，参数只能是时间戳
# a = time.localtime(2019)
# print(a)
# #本地化默认显示当前时间、
# 可以传入参时，占位符填充的就是参数的时间，参数只能时元组的时间
# a = time.strftime('%Y-%m-%d  %H:%M:%S %w')
#将元组类型的时间转化为本地格式时间
# a = time.strftime('%Y-%m-%d  %H:%M:%S %w',time.localtime(000))
#将本地化时间转化为元组时间
#第一个参数是本地化时间
#第二格时间占位符时间
# a = time.strptime('2018-12-27  10:56:00','%Y-%m-%d  %H:%M:%S')
# print(a)

#休息
# time.sleep(1000)
#将元组的时间转换成书间戳
# b = (2018,12,13,14,12,11123,1213,31,10)
# a = time.mktime(b)
# print(a)

#判断今年是不是闰年，第几天，几月
# import  time
 # r = input(">>>")
 # qi = time.strptime(r,'%Y-%m-%d  %H:%M:%S')
 # x = qi[0]
# y = str(x)
 # print(y)

# if  y[2] =='0'and y[3]=='0':
#     k=x%400
#     if  k==0:
#         print('闰年')
#     else:
#         print('不是闰年')
# elif y[2] !='0' or  y[3] !='0':
#     t=x%4
#     if  t==0:
#         print('闰年')
#     else:
#         print('不是闰年')
# print('今年第几月{}'.format(qi[1]))
# print('今年第几天{}'.format(qi[7]))

#将b.txt文件追加到cj.txt中

# with open('c.txt','r',encoding='utf-8') as f:
#     a = f.readlines()
#     print(a)
# with open('cj.txt','a',encoding='utf-8') as f:
#     for i in a:
#        f.write(i)


#将yy.xls追加到b.txt文件中
# from xlutils.copy  import copy
# import xlrd
# f = xlrd.open_workbook('yy.xls')
# sheet = f.sheet_by_name('sheet1')
# b = sheet.nrows
# # print(b)
# with open('b.txt','w',encoding='utf-8') as kk:
#     for  i in range(b):
#         c = sheet.row_values(i)
#         kk.write('{}'.format(c))
#         kk.write('\n')

#对数据库的操作
# import pymysql
#连接数据库
# conn = pymysql.connect(host='192.168.0.86',
#                        port=3306,
#                        user='root',
#                        passwd='123456')
# # #创建一个游标
# m = conn.cursor()
#执行sql语句
# m.execute("create database  python_xuexi1;")
# m.execute('use  python_xuexi;')
# m.execute('show  databases;')

# print(m.fetchall())
# m.execute('show  tables')
# # m.execute('drop   table shuju1')
# m.execute('create   table   biao7  (name  char(20),age  int,sex  char(10));')
# # m.execute('show  tables;')
# for i in range(20):
#        m.execute('insert  into  biao7  values("{}",{},"{}")'.format(i))
#        m.execute('select * from  biao7;')
# # m.execute('select * from biao3;')
# #读取数据路(查看上一个命令的结果是一个元组)
# b = m.fetchall()
#默认一次只读取一个数据，传入的参数是几就读取就条数据
# b = m.fetchmany()
#每次只读取一行，有多少就读多少，按照顺序读取
# b = m.fetchone()
# b = m.fetchall()
# print(b)

#将excel表中的数据读取到数据库中
# import xlrd
# f = xlrd.open_workbook('yy.xls')
# m.execute('use  test1;')
# sheet = f.sheets()[0]
# for  i in range(sheet.nrows):
#     b = sheet.row_values(i)
#     if i == 0:
#         continue
#         m.execute('create  table  shuju({} char(255),{}  int,{}  char(255),{}  int)'.format(b[0],b[1],b[2],b[3]))
#     else:
#         m.execute('insert  into  shuju  values("{}","{}","{}","{}")'.format(b[0],b[1],b[2],b[3]))
# m.execute('select  * from   shuju;')
# c = m.fetchall()
# print(c)

#将文档中的数据读取到数据库中
# import xlrd
# import pymysql
# conn = pymysql.connect(host='192.168.0.86',
#                        port=3306,
#                        user='root',
#                        passwd='123456')
# m = conn.cursor()
# f = open('cj.txt','r',encoding='utf-8')
# m.execute('use  test1;')
# b = f.readlines()
# print(len(b))
# for i  in  range(len(b)):
#     c = b[i]
#     c=c.split(',')
#     print(c)
#     if i==0:
#       continue
#       m.execute('create  table  shuju3({} char(255),{}  int,{}  char(255),{}  int)'.format(c[0],c[1],c[2],c[3]))
#     else:
#       m.execute('insert  into  shuju3  values("{}","{}","{}","{}")'.format(c[0],c[1],c[2],c[3]))
# m.execute('select  * from   shuju3;')
# c = m.fetchall()
# print(c)

# 与操作系统交互的模块
# import os

#获取当前位置
# print(os.getcwd())
#切换目录
# os.chdir(r'C:\user\work')
# print(os.getcwd())
#执行cmd命令,有结果的命令
# b = os.popen('ping 192.168.0.26')
# print(b.read())
#获取当前目录下的所有文件,可以传入参数：是以个路径
# print(os.listdir(r'C:\work'))
#创建目录，也可以加目录
# os.mkdir(r'C:\work',)
#删除目录
# os.rmdir('aaa')
#创建递归目录
# os.makedirs(r'aaa\bb\c')
#删除递归目录
# os.removedirs(r'aaa\bb\c')
# #将路劲与文件分离开
# b = os.path.split(r'C:\work')
#奖后缀名与路径分开
# b = os.path.splitext(r'D:\work\untitled\venv\tt.jpeg')
#
# print(b[1])

#判断是否是普通文件
# b = os.path.isfile(r'D:\Users\xiaoxiannv\AppData\Local\Youdao\Dict')
# print(b)

#将目录下所有。py的文件打印出来
# a = print(os.getcwd())
# print(a)
# b = os.listdir()
# for i in range(len(b)):
#     c = os.path.splitext('{}'.format(b[i]))
#     if  c[1]=='.py':
#         print(b[i])

# import paramiko
# #创建一个ssh客户端
# with paramiko.SSHClient() as ssh111:
# #跳过know-hosts文件中验证
#      ssh111.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# #连接主机
#      ssh111.connect(hostname='192.168.0.117',
#                port=22,
#                username='root',
#                password='123456')
# #执行命令
#      while True:
#          x=input('>>>')
#          if x == 'exit':
#              break
#          else:
#
#              a,b,c=ssh111.exec_command('{}'.format(x))
# # 第一个变量：标准输入的命令(不能简写，必须是有结果的命令
# # 第二个变量：是命令的输出
# # 第三个变量是命令的报错
#              print(b.read().decode())
# # 断开连接
# ssh111.close()
# # #上传和下载文件
# import paramiko
# # #创建一个传输通道
# qq = paramiko.Transport(('192.168.0.117',22))
# # #连接主机
# qq.connect(username='root',password='123456')
# # #使用ssh协议创建一个传输功能
# sftp = paramiko.SFTPClient.from_transport(qq)
# # #下载文件，从Linux上下载到window
# sftp.get(r'/home/b.sh','qqq.sh')
# # #上传文件，从window上传到Linux上
# sftp.put('xixi.py','/home/day3.py')
# # #断开连接`--
# qq.close()






#发送邮件 smtp  pop3   imap
# import smtplib     #封装了smtp协议
# import email.mime.multipart as mul    #制作邮件
# import email.mime.text  as  text    #对邮件的正文经行处理
# #创建一个空邮件
# message = mul.MIMEMultipart()
# #标题
# message['Subject']='python_test'
# #发件人
# tt='15226018652@163.com'
# message['From']=tt
# #收件人
# w = ['dingyuchang@163.com','15226018652@163.com']
# message['To'] = '.'.join(w)    #群发格式
# #正文  多行数据
# txt = """"
# 小昭
# 倚天屠龙
# 中南山下活死人墓
# """
# #对正进行处理
# tet = text.MIMEText(txt)
# #将处理后的正文添加到邮件里
# message.attach(tet)
# #带有附件的邮件
# att1 = text.MIMEText(open('cj.txt', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="cj.txt"'
# message.attach(att1)
# #
# #
# # #定义一个邮件服务器
# smtp123 = smtplib.SMTP_SSL('smtp.163.com',465)   #后面的是端口号
# #登录服务器  用户名，密码（不是邮箱密码，是授权码）
# smtp123.login('15226018652@163.com','ghy1227')
# #发送邮件   发送者   接受者
# smtp123.sendmail(tt,w,message.as_string())
# #断开连接
# smtp123.close()

# socket  是基于TCP的
# 套接字，提供了通信双方最底层的功能(发送和接受)
#一般C/S架构  通过socket实现最基本的通信

# #server端  服务器
# import  socket
# #创建一个套接字（具有发送和接受能力）
# #SOCK_STREAM  指的是tcp  AF_INET  指的是ipv4
# s  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #需要给套接字绑定ip和端口号
# s.bind(('192.168.0.66',3000))
# #监听
# s.listen(3)
# while True:
#     #接受客户端建立的连接
#     #接受的是建立连接，第一个变量的结果：建立连接的信息。第二个变量结果：客户端的IP地址和端口号
#     client,addr = s.accept()
#     #接受客户端发送的数据
#     #1024指的是每次能够接受的最大数据字节，可以写其它的但是不能超过1024
#     reg = client.recv(1024)
#     print(reg.decode('utf-8'))
#     msg = input(">>>")
#     #给客户端发送响应
#     client.send(msg.encode('utf-8'))

#udp服务器
# import socket
# #创建一个套接字
# #ipv4      SOCK_DGRAM....是udp
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #绑定IP地址
# s.bind(('192.168.0.66',3000))
#
# while True:
#     # 接受客户端的请求
#     #第一个变量：客户端的请求数据
#     #第二个变量：是客户端的IP和端口号
#     client,addr = s.recvfrom(1024)
#     print(client.decode('utf-8'))
#     #发送响应
#     msg = input('>>>')
#     s.sendto(msg.encode('utf-8'),addr)

#python函数
# print(hex(342))     #10进制转16进制
# print(oct(534))     #10进制转8进制
# print(bin(423))     #10进制转2进制
# print(int(0b110100111))  #任何进制转10进制

#chr将数字转化为asill表中对应的字符
# a = [chr(i)  for  i in range(56,123)]
# print(a)
#ord 将asill表中的字符转换成对应的数字
# print(ord('\\'))
# a = [23,35,132,4656]
# print(sum(a))
#整除求余
# a,b = divmod(100,16)
# print(a,b)





