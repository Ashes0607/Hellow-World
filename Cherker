# coding=UTF-8
import csv

with open(r'C:\Users\wb.miaotianze\Desktop\特技表.csv') as f:
    reader = csv.DictReader(f)
    column = [row['BUFF1']for row in reader]
    # rows = [row for row in reader]
    # print(column)
    # 方法2 读取csv第一行
    # head_row = next(reader)
    # print(head_row)
    # 读取文件某一列数据
    # reader = csv.reader(f)
    # column = [row[0] for row in reader]
    # print(column)


with open(r'C:\Users\wb.miaotianze\Desktop\状态数据表.csv') as f:
    reader = csv.DictReader(f)
    column2 = [row['状态编号']for row in reader]
    # print(column2)

# a 在表1，不在表2

a = [x for x in column if x not in column2]

# b 在表2，不在表1

b = [y for y in column2 if y not in column]
# for i in a:
#     print(i)
    # with open(r'C:\Users\wb.miaotianze\Desktop\不在表2.xlsx', 'a')as f:
    #     f.write('%sn'%i)

print('差异数量a: ', len(a))
print('差异数量b: ', len(b))
print('在表2，不在表1的值: ', b)

