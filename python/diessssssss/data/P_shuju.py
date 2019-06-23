import xlrd

def PJ_shuju():
    num_2 = []
    f = xlrd.open_workbook(r'D:/work/untitled/diessssssss/data/chaxun.xlsx')
    sheet = f.sheets()[0]
    for i in range(sheet.nrows):
        num_2.append(sheet.row_values(i))
    return num_2

if __name__ == '__main__':
    print(PJ_shuju())




