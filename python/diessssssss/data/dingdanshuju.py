import xlrd
from diessssssss.config import dingdan

def shuju():
    num_1 = []
    f = xlrd.open_workbook(r'D:\work\untitled\diessssssss/data/bieke_test.xlsx')
    sheet= f.sheets()[0]
    for i in range(sheet.nrows):
        num_1.append(sheet.row_values(i))

    return num_1

if __name__ == '__main__':
    print(shuju())