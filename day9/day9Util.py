import pymysql
import xlrd
import xlwt
host="localhost"
user="root"
password="root"
database="newday"
def save(sql,param):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql,param)
    con.commit()
    cursor.close()
    con.close()
    pass

def sel(sql):
    con = pymysql.connect(host = host,user = user,password = password,database = database)
    cursor = con.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    con.close()
    return data

def countyf(sql):
    con = pymysql.connect(host = host,user = user,password = password,database = database)
    cursor = con.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    cursor.close()
    con.close()
    return data[0]

def seltion(table):
    sql = "select * from" + table
    return sel(sql)

def count(table):
    sql = "select count(*) from " + table
    return countyf(sql)

def excel_to_db(filename,sheet,table):
    wd = xlrd.open_workbook(filename=filename, encoding_override=True)
    st = wd.sheet_by_name(sheet)
    rows = st.nrows
    cols = st.ncols
    rs = st.row_slice(0)
    max2 = len(rs)
    for i in rs:
        if i == "":
            max2 = max2 - 1
            pass
        elif i == None:
            max2 = max2 - 1
            pass
        pass
    for i in range(1, rows):
        param = []
        for j in range(0,max2-1):
            param.append(st.cell_value(i, j))
        sql = "insert into" + table + "values(%s"
        for x in range(1,max2-1):
            sql+= ",%s"
            pass
        sql+=")"
        save(sql, param)
        pass
    print("excel_to_DB")
    pass

def db_to_excel(filename,newsheet,table):
    # 创建一个workbook 设置编码
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet(newsheet)
    # 写入excel
    max = count(table)
    data = seltion(table)

    for i in range(1, max):
        max1 = len(data[i - 1]) - 1
        for j in range(0, int(max1)):
            # 参数对应 行, 列, 值
            worksheet.write(i, j, label=data[i - 1][j + 1])
        pass
    # 保存
    workbook.save(filename)
    print("DB_to_excel")

