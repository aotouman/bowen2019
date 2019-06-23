#!/use/bin/python
#-*- conding:utf-8 -*-

from HTMLTestReportCN import HTMLTestRunner
import unittest

def cxun_mx(name):
    suit = unittest.TestSuite()
    for i in name:
        cx = unittest.defaultTestLoader.discover(r'D:/work/untitled/diessssssss/test/',pattern='{}test.py'.format(i.strip()))
        for j in cx:
            suit.addTest(j)
            f = open('chaxun.html','wb')
            runner = HTMLTestRunner(stream=f,tester='ghy',description='结果如下',title='别克查询明细')
            runner.run(suit)
            f.close()

if __name__ == '__main__':
    cxun_mx('*')












