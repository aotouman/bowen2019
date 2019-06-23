#!/use/bin/python
#-*- conding:utf-8 -*-

from HTMLTestReportCN import HTMLTestRunner
import unittest
# from diessssssss.data.dingdanshuju import shuju

#出现不能用的原因是，pycham本身自带了一个unittest
def B_gao(name):
    #创建一个测试套件
    suit = unittest.TestSuite()
    #将测试用例添加到测试套件里
    #将某一个人类中所有
    # suit.addTest(unittest.makeSuite())
    #第一个参数：存放测试脚本的路劲
    #第二个参数：匹配测试文件的通配符语句
    #函数语句意思自动去发现通配符语句中符合统配符的文件中以test开头的函数，提取出放在dis列表中
    for i in name:

       dis = unittest.defaultTestLoader.discover(r'D:\work\untitled\diessssssss\test',pattern='{}test.py'.format(i.strip()))
    # print(dis)
       for i in dis:
          suit.addTest(i)

       f = open('bk.html','wb')
       runner = HTMLTestRunner(stream=f,tester='ghy',description='结果如下',title='别克测试报告')
       runner.run(suit)
       f.close()

if __name__ == '__main__':
     B_gao('*')














