#day15_以下文件是用户的一些数据（姓名、年龄、净资产），要求使用数据库工具将文件中的数据写入到数据库中。并统计所有人的资产总和！


import pymysql
host="localhost"
user="root"
password="root"
database="newday"
def usercount():
    sqlcount = "select sum(meny) from day15_1"
    return usercountUtil(sqlcount)
def usercountUtil(sql):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    cursor.close()
    con.close()
    return data[0]
def saveorupdUtil(sql,param):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    if param != None:
        cursor.execute(sql,param)
        pass
    else:
        cursor.execute(sql)
        pass
    con.commit()
    cursor.close()
    con.close()
    pass
f = open(r"G:\python\day15任务\用户数据.txt" , mode = "r+" ,encoding="GBK")
namelist=[]
agelist=[]
menylist=[]
for i in [i.split(",") for i in f.readlines()]:
    namelist.append(i[0])
    agelist.append(i[1])
    menylist.append(i[2])
for j in range(0, len(namelist)-1):
    param = [namelist[j],agelist[j],menylist[j]]
    sql = "insert into day15_1 values(%s,%s,%s)"
    saveorupdUtil(sql,param)
    param.clear()
    pass

print(usercount())



