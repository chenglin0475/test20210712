import xlrd
import xlwt
from day9Util import *

class inmation:
    def __init__(self,id,tian,fname,danjia,shuliang,risale):
        self.id = id
        self.tian = tian
        self.fname = fname
        self.danjia = danjia
        self.shuliang = shuliang
        self.risale = risale
        pass
    pass
    def __init__(self,tian,fname,danjia,shuliang,risale):
        self.tian = tian
        self.fname = fname
        self.danjia = danjia
        self.shuliang = shuliang
        self.risale = risale
        pass
    pass

# def maketion(self):
#     param = [self.tian,self.fname,self.danjia,self.shuliang,self.risale]
#     sql = "insert into yfsale12(tian,fname,danjia,shuliang,risale)values(%s,%s,%s,%s,%s)"
#     save(sql,param)
#     pass

filename="12月份衣服销售数据.xlsx"
sheet = "12月份各种服饰销售情况"
table = " yfsale12 "
filename1="12月份衣服销售数据1.xlsx"
sheet1 = "新sheet"
excel_to_db(filename,sheet,table)
db_to_excel(filename1,sheet1,table)
# wd = xlrd.open_workbook(filename="12月份衣服销售数据.xlsx", encoding_override=True)
# st = wd.sheet_by_name("12月份各种服饰销售情况")
# rows = st.nrows
# cols = st.ncols
# for i in range(1,rows):
#     tian = st.cell_value(i,0)
#     fname = st.cell_value(i,1)
#     danjia = float(st.cell_value(i,2))
#     shuliang = int(st.cell_value(i,3))
#     risale = int(st.cell_value(i,4))
#     saleobeject = inmation(tian,fname,danjia,shuliang,risale)
#     maketion(saleobeject)
#     pass
# print("excel_to_DB")
# # 创建一个workbook 设置编码
# workbook = xlwt.Workbook(encoding = 'utf-8')
# # 创建一个worksheet
# worksheet = workbook.add_sheet('新sheet')
# # 写入excel
# max = count()
# data = seltion()
#
# for i in range(1,max):
#     max1 = len(data[i - 1])-1
#     for j in range(0,int(max1)):
#         # 参数对应 行, 列, 值
#         worksheet.write(i, j, label=data[i-1][j+1])
#     # worksheet.write(i, 1, label=data[i-1][2])
#     # worksheet.write(i, 2, label=data[i-1][3])
#     # worksheet.write(i, 3, label=data[i-1][4])
#     # worksheet.write(i, 4, label=data[i-1][5])
#     pass
# # 保存
# # workbook.save('D:\PythonTool\test\day9\12月份衣服销售数据1.xlsx')
# workbook.save('12月份衣服销售数据1.xlsx')
# print("DB_to_excel")





