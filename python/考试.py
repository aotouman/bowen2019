#!/usr/bin/python
#-*- conding:utf-8 -*-
#九九乘法表、
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{}*{}={}'.format(i,j,i*j),end='\t')
#     print()
#不用int将字符串变成整数
# a = input('>>')
# b = len(a)
# c = 0
# for i in range(b):
#     for j in range(10):
#         if str(j) == a[i]:
#            c += j*10**(b-i-1)
# print(c)
# print(type(c))
#创建一个aaa目录，在创建一个a.txt文件，向a.txt文件中写入多行内容
# import os
# # os.mkdir('aaa')
# with open(r'aaa\a.txt','w',encoding='utf-8') as f:
#     f.write('sgestgewvdvf\n''fqrdfseqwtf\n')
# with open(r'aaa\a.txt','r',encoding='utf-8') as ff:
#     a = ff.readlines()
#     print(a)
# os.remove(r'aaa\a.txt')
# os.rmdir('aaa')
#将a.txt文件 中的数据添加到数据库中
# import pymysql
# import xlrd
# conn = pymysql.connect(host='192.168.0.89',
#                        port=3306,
#                        user='root',
#                        passwd='123456')

# m = conn.cursor()
# f = open('cj.txt','r',encoding='utf-8')
# m.execute('use  python_kaoshi')
#
# b = f.readlines()
# # print(len(b))
# for i  in  range(len(b)):
#     c = b[i]
#     c=c.split(',')
#     # print(c)
#     if i==0:
#       continue
#       m.execute('create  table  kaoshi({} char(255),{}  int,{}  char(255),{}  int)'.format(c[0],c[1],c[2],c[3]))
#     else:
#       m.execute('insert  into  kaoshi  values("{}","{}","{}","{}")'.format(c[0],c[1],c[2],c[3]))
# m.execute('select  * from   kaoshi;')
# c = m.fetchall()
# # print(c)

#socket的永久通信服务器
# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('192.168.0.58',3000))
# s.listen(3)
# while True:
#     client,addr = s.accept()
#     reg = client.recv(1024)
#     print(reg.decode('utf-8'))
#     msg = input('>>>')
#     client.send(msg.encode('utf-8'))
#
# import smtplib
# import email.mime.multipart as mul
# import email.mime.text as text
# massage = mul.MIMEMultipart()
# massage['subject'] = 'python_ghy'
# massage['From']='15226018652@163.com'
# massage['To']='825069672@qq.com'
# txt = """钟南山下，活死人墓。
#          神雕侠侣，绝迹江湖"""
# tet = text.MIMEText(txt)
# att1 = text.MIMEText(open('c.txt','rb').read(),'base64','utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# att1["Content-Disposition"] = 'attachment; filename="c.txt"'
# massage.attach(att1)
#

# import requests
# import json
# url='https://fe-api.zhaopin.com/c/i/sou?start=90&pageSize=90&cityId=538&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&kt=3&=0&_v=0.80226492&x-zp-page-request-id=f14ab29fd9c84c6987a2d1a82d7259ab-1557219520461-956404'
# head={'User-Agent':'Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
# res = requests.get(url,headers=head)
# p=res.content.decode('utf-8')
# aa = json.loads(p)
# f=open('b.txt','w+',encoding='utf-8')
# for  i in range(0,90):
#     b1=aa['data']['results'][i]['company']['name']
#     b2=aa['data']['results'][i]['jobName']
#     b3=aa['data']['results'][i]['salary']
#     b4=aa['data']['results'][i]['city']['display']
#     b5=aa['data']['results'][i]['eduLevel']['name']
#     f.write("{},".format(b1))
#     f.write("{},".format(b2))
#     f.write("{},".format(b3))
#     f.write("{},".format(b4))
#     f.write("{}".format(b5))
#     f.write('\n')
# f=open('b.txt','r',encoding='utf-8')
# a=f.readlines()
# import pymysql
# import xlwt
# ww=xlwt.Workbook('a5.xls')
# sheet=ww.add_sheet('qiuzhi')
# c=["公司ID","岗位名称","薪资","公司地点","学历"]
# for k in range(len(c)):
#     sheet.write(0,k,c[k])
# for l in range(0,len(a)):
#     bb=a[l].split(',')
#     for a1 in range(len(c)):
#         sheet.write(l+1,a1,bb[a1])
# ww.save('a.xls')
# conn=pymysql.connect(host='192.168.0.89',port=3306,user='root',passwd='123456')
# m=conn.cursor()
# m.execute('use python_kaoshi')
# m.execute('create table qiuzhi(公司ID  char(45),岗位名称 char(35),薪资 char(15),公司地点 char(10),学历 char(10))')
# for j in range(0,len(a)):
#     bb=a[j].split(',')
#     m.execute('insert into qiuzhi values("{}","{}","{}","{}","{}");'.format(bb[0],bb[1],bb[2],bb[3],bb[4]))


# import os
# import xlrd
# import xlwt
# import smtplib
# os.mkdir('ppt')
# ppt = xlwt.Workbook(encoding='utf-8')
# sheet = ppt.add_sheet('python_test')
# for i in range(1,10):
#     for j in range(1,i+1):
#         sheet.write(i-1,j-1,'{}*{}={}'.format(i,j,i*j))
# ppt.save(r'ppt\pt.xls')
# with open(r'ppt\ppt.txt','w',encoding='utf-8') as tt:
#      pp = xlrd.open_workbook(r'ppt\pt.xls')
#      t = pp.sheet_names()
#      sheet = pp.sheet_by_name('python_test')
#      b = sheet.nrows
#      for i in range(b):
#          p = sheet.row_values(i)
#          c = str(p)
#          d = ''.join(c)
#          tt.write(d)
#          tt.write('\n')
# import email.mime.multipart as mul
# import email.mime.text  as text
# message = mul.MIMEMultipart()
# message['subject'] = 'python-ppt'
# message['From'] = '15226018652@163.com'
# message['To'] = '2446607275@qq.com'
# txt = """终南山下，活死人墓。
#          神雕侠侣，绝技江湖。"""
# tet = text.MIMEText(txt)
# message.attach(tet)
# att1 = text.MIMEText(open(r'ppt\ppt.txt', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# att1["Content-Disposition"] = 'attachment; filename="c.txt"'
# message.attach(att1)

# import requests
# import re
# import json
# url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=软件测试&kt=3&_v=0.49248174&x-zp-page-request-id=c2002d7c45ab4c82a3cbce109918d10b-1557307398345-311035'
# head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
# res = requests.get(url,headers = head)
# hh = res.content.decode('utf-8')
# aa = json.loads(hh)
# with  open(r'zhilian.txt','w',encoding='utf-8') as zz:
#     for i in range(90):
#         a1=  aa['data']['results'][i]['company']['name']
#         a2=  aa['data']['results'][i]['city']['display']
#         a3=  aa['data']['results'][i]['salary']
#         a4=  aa['data']['results'][i]['jobName']
#         zz.write('{},'.format(a1))
#         zz.write('{},'.format(a2))
#         zz.write('{},'.format(a3))
#         zz.write('{}'.format(a4))
#         zz.write('\n')
# with open('zhilian.txt','r',encoding='utf-8') as f:
#     b = f.readlines()
#     print(b)
# import xlwt
# import xlrd
# ff = xlwt.Workbook(encoding='utf-8')
# sheet = ff.add_sheet('python_test')
# c = ['公司名称','地点','薪资','岗位']
# for k in range(len(c)):
#     sheet.write(0,k,c[k])
# for j in range(len(b)):
#     bb = b[j].split(',')
#     for h in range(len(c)):
#         sheet.write(j+1,h,bb[h])
# ff.save('zhilain.xls')

# import requests
# import re
# class shock():
#     def sen(self,i):
#         url = 'http://fabiaoqing.com/biaoqing/lists/page/{}.html'.format(i)
#         head = {'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}
#         res = requests.post(url)
#         hh = res.content.decode('utf-8')
#         return hh
#
#     def guolv(self,y):
#         title = []
#         pat = re.compile(' <img class="ui image lazy" data-original="(.*?)" title="(.*?)"')
#         a=pat.findall(y)
#         for j in range(1):
#             c=requests.get(a[j][0])
#             d=c.content
#             f=open(r'{}.jpg'.format(a[j][1]),'wb')
#         ff=open(r'{}.jpg'.format(a[0]),'w+',encoding='utf-8')
#
#             f.write(d)
#             f.close()
#
# tt=shock()
# for i in range(1,2):
#     hh=tt.sen(i)
#     yy=tt.guolv(hh)
#     tt.save(yy)
#
# aa=shock()
# hh=aa.sen(3)
# aa.guolv(hh)


# import  unittest    #写单元测试用的，写断感言用的
# #断言：根据预期结果那实际结果作对比的过程
# class  Demo(unittest.TestCase):
#
#     def test_1(self):
#         #假设预期结果是1
#         #实际结果是2
#         #判断预期结果是否等于实际结果
#         a = 1   #预期结果
#         #断言
#         self.assertEqual(a,2)
#
# if  __name__=='__main__':
#     unittest.main()

# import xlrd
# import xlwt
# f = xlwt.Workbook('utf-8')
# sheet = f.add_sheet('python-test')
# with  open(r'a.txt','w',encoding='utf-8') as  t:
#
#     for  i  in range(1,10):
#         for j in range(1,i+1):
#                t.write('{}*{}={}\t'.format(i,j,i*j))
#         t.write('\n')
# with  open(r'a.txt','r',encoding='utf-8') as p:
#     y=p.readlines()
#
#     for x in range(len(y)):
#         a=y[x].split('\t')
#         for i in range(len(a)):
#             sheet.write(x,i,a[i])
# f.save('aa.xls')

import  pymysql
import  xlwt
conn = pymysql.connect(host='192.168.0.124',port=3306,user='root',passwd='123456')
# a=xlwt.Workbook('a1.xls')
# b=a.add_sheet('test')
# b.write(0,0,'name')
# b.write(0,1,'sex')
# b.write(0,2,'id')
# b.write(0,3,'kemu')
# a.save('a1.xls')
m.conn.cursor()
m.execute("create  database  python_day1;")
m.execute("use  python_day1;")

sheet = m.sheets()[0]
for i in range(sheet,nrows):
    b = sheet.row-valuse(i)
    if i==0:
        continue
        m.execute("'(create  table day1({}  char(20),{}  char(),{} int(),{}  char())'.format(b[0],b[1],b[2],b[3])")
    else:
        m.execute("insert  imto  day1  valuse(('{}','{}','{}','{}').format(b[0],b[1],b[2],b[3])")
m.save()





