#!/use/bin/python
#-*- conding:utf-8 -*-

from diessssssss.report.chax import cxun_mx
with open(r'D:/work/untitled/diessssssss/data/a.txt','r') as f:
    a = f.readlines()
    if 'all' in a:
        cxun_mx('*')
    else:
        cxun_mx(a)

