#!/use/bin/python
#-*- conding:utf-8 -*-

from HTMLTestReportCN import HTMLTestRunner
import unittest

def peijian_mx():
    suit = unittest.TestSuite()
    # for i in name:
    cx = unittest.defaultTestLoader.discover(r'D:/work/untitled/diessssssss/test/',pattern='peijian_test.py')
    # for j in cx:
    suit.addTest(cx)
    f = open(r'D:\work\untitled\diessssssss\report\aa.html','wb')
    runner = HTMLTestRunner(stream=f,tester='ghy',description='结果如下',title='别克查询明细')
    runner.run(suit)
    f.close()

if __name__ == '__main__':
    peijian_mx()