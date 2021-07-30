import pymysql

host="localhost"
user="root"
password="root"
database="newday"
def booleanuserUtil(sql,param):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql, param)
    data = cursor.fetchone()
    cursor.close()
    con.close()
    if data == None :
        return False
    else :
        return True
    pass

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

def selectuserUtil(sql,param):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql,param)
    data = cursor.fetchone()
    return data
