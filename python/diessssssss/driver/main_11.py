#!/use/bin/python
#-*- conding:utf-8 -*-

#driver中主要控制跑回归测试是只跑哪些模块的用例

from diessssssss.report.baogao import B_gao

with open(r'D:/work/untitled/diessssssss/data/a.txt','r') as f:
    a = f.readlines()
    if 'all' in a:
        B_gao('*')
    else:
        B_gao(a)





























