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

def maketion(self):
    param = [self.tian,self.fname,self.danjia,self.shuliang,self.risale]
    sql = "insert into yfsale12(tian,fname,danjia,shuliang,risale)values(%s,%s,%s,%s,%s)"
    save(sql,param)
    pass
def seltion():
    sql = "select * from yfsale12"
    return sel(sql)
def count():
    sql = "select count(*) from yfsale12"
    return countyf(sql)

wd = xlrd.open_workbook(filename="12月份衣服销售数据.xlsx", encoding_override=True)
st = wd.sheet_by_name("12月份各种服饰销售情况")
rows = st.nrows
cols = st.ncols
for i in range(1,rows):
    tian = st.cell_value(i,0)
    fname = st.cell_value(i,1)
    danjia = float(st.cell_value(i,2))
    shuliang = int(st.cell_value(i,3))
    risale = int(st.cell_value(i,4))
    saleobeject = inmation(tian,fname,danjia,shuliang,risale)
    maketion(saleobeject)
    pass
print("excel_to_DB")
# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding = 'utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('新sheet')
# 写入excel
max = count()
data = seltion()
worksheet.write(0, 0, label="日期")
worksheet.write(0, 1, label="服装名称")
worksheet.write(0, 2, label="价格/每件")
worksheet.write(0, 3, label="单价")
worksheet.write(0, 4, label="单日销量")
for i in range(1,max):
    j = i - 1
    # 参数对应 行, 列, 值
    worksheet.write(i, 0, label=data[j][1])
    worksheet.write(i, 1, label=data[j][2])
    worksheet.write(i, 2, label=data[j][3])
    worksheet.write(i, 3, label=data[j][4])
    worksheet.write(i, 4, label=data[j][5])
    pass
# 保存
# workbook.save('D:\PythonTool\test\day9\12月份衣服销售数据1.xlsx')
workbook.save('12月份衣服销售数据1.xlsx')
print("DB_to_excel")





