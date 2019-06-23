#!/use/bin/python
#-*- conding:utf-8 -*-



from diessssssss.report.peijiang import peijian_mx
with open(r'D:/work/untitled/diessssssss/data/a.txt','r') as f:
    a = f.readlines()
    if 'all' in a:
        peijian_mx('*')
    else:
        peijian_mx(a)