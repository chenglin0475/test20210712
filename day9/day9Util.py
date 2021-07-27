import pymysql

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

