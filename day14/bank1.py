'''
    中国工商银行账户管理系统：
        ICBC:
'''
import datetime
import random
from DBUtil import *
# 1.准备一个数据库 和 银行名称
import pymysql
import time

# 1.连接数据库
con = pymysql.connect(host="localhost", user="root", password="root", database="newday")
# 2.创建控制台
cursor = con.cursor()
# bank = {}  # 空的数据库
# '''
#     {
#         "s001":{
#             "张三":"张三",
#             country:"中国"
#         }，
#         "s002":{
#
#         }
#
#
#     }
#
# '''
bank_name = "中国工商银行昌平回龙观支行"  # 银行名称写死的

global loginid
loginid = 0


class bank_user:
    userCount = 0

    def __init__(self, account, username, password, country, province, street, door, money, registerDate, bankname):
        self.account = account
        self.username = username
        self.password = password
        self.country = country
        self.province = province
        self.street = street
        self.door = door
        self.money = money
        self.registerDate = registerDate
        self.bankname = bankname
        bank_user.userCount +=  1
        pass

    pass
param = []
# #打包主键在最后
# def paramforupd(self):
#     param = [self.username,self.password,self.country, self.province, self.street, self.door, self.money, self.bankname,self.account]
#     return param
#打包主键主键在第一位
def paramforinsert(self):
    # time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    param = [self.account,self.username,self.password,self.country, self.province, self.street, self.door, self.money, create_time, self.bankname]
    return param
#查询用户是否存在
def booleanuser(account):
    parambo = [str(account)]
    sqlcha = "select * from bank_user where account = %s"
    return booleanuserUtil(sqlcha,parambo)
    # cursor.execute(sqlcha)
    # data = cursor.fetchone()
    # if data != None:
    #     return True
    # else:
    #     return False
    # pass
#查询数据库中用户的数量
def usercount():
    sqlcount = "select count(*) from bank_user"
    return usercountUtil(sqlcount)
    # cursor.execute(sqlcount)
    # data = cursor.fetchone()
    # return data[0]

#保存或修改用户信息
def saveorupd(self):

    insql = "insert into  bank_user values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    #def __init__(self, account, username, password, country, province, street, door, money, registerDate, bankname):
    updsql = "update bank_user set " \
             # "username = %s,password = %s,country = %s,province = %s," \
             # "street = %s,door = %s,money = %s,bankname = %s " \
             # "where account = %s "
    if booleanuser(self.account):
        if self.username != None:
            updsql += " username = '" + self.username + "'"
            pass
        if self.password != None:
            updsql += " ,password = '" + self.password + "'"
            pass
        if self.country != None:
            updsql += " ,country = '" + self.country + "'"
            pass
        if self.province != None:
            updsql += " ,province = '" + self.province + "'"
            pass
        if self.street != None:
            updsql += " ,street = '" + self.street + "'"
            pass
        if self.door != None:
            updsql += " ,door = '" + self.door + "'"
            pass
        if self.money != None:
            updsql += " ,money = " + str(self.money)
            pass
        if self.bankname != None:
            updsql += " ,bankname = '" + self.bankname + "'"
            pass
        updsql += " where account = " + self.account
        saveorupdUtil(updsql,None)
        # cursor.execute(updsql)
        pass
    else:
        saveorupdUtil(insql,paramforinsert(self))
        # cursor.execute(insql,paramforinsert(self))
        pass
    # con.commit()
    pass
def selectuser(account):
    paramse = [str(account)]
    selsql = "select * from bank_user where account = %s"
    data = selectuserUtil(selsql,paramse)
    # cursor.execute(selsql)
    # data = cursor.fetchone()
    user = bank_user(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9])
    return user




# 2.入口程序
def welcome():
    print("*************************************")
    print("*      中国工商银行昌平支行           *")
    print("*************************************")
    print("*  1.开户                            *")
    print("*  2.存钱                            *")
    print("*  3.取钱                            *")
    print("*  4.转账                            *")
    print("*  5.查询                            *")
    print("*  6.Bye！                           *")
    print("**************************************")


# 银行的开户逻辑
def bank_addUser(account, username, password, country, province, street, gate, money):
    localtime = time.asctime(time.localtime(time.time()))
    maker = bank_user(account,username,password,country,province,street,gate,money,localtime,bank_name)
    # 1.判断数据库是狗已满
    if usercount() >= 100:
        return 3
    # 2.判断用户是否存在
    if booleanuser(account):
        return 2
    # 3.正常开户
    saveorupd(maker)
    return 1


# 用户的开户的操作逻辑
def addUser():
    username = input("请输入您的用户名：")
    password = input("请输入您的开户密码：")
    country = input("请输入您的国籍：")
    province = input("请输入您的居住省份：")
    street = input("请输入您的街道：")
    gate = input("请输入您的门牌号：")
    money = int(input("请输入您的开户初始余额："))  # 将输入金额转换成int类型
    # 随机产生8为数字
    account = random.randint(10000000, 99999999)
    if booleanuser(str(account)):
        account = random.randint(10000000, 99999999)
    status = bank_addUser(str(account), username, password, country, province, street, gate, money)

    if status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")
    elif status == 2:
        print("对不起，该用户已存在！请勿重复开户！")
    elif status == 1:
        print("开户成功！以下是您的个人开户信息：")
        info = '''
            ----------个人信息------
            用户名：%s
            密码：%s
            账号：%s
            地址信息
                国家：%s
                省份：%s
                街道：%s
                门牌号: %s
            余额：%s
            开户行地址：%s
            ------------------------
        '''
        print(info % (username, password, account, country, province, street, gate, money, bank_name))
        # bank[account] = (username, password,country, province, street, gate, money, bank_name)
        # bank[account]["username"] = username
        # bank[account]["password"] = password
        # bank[account]["country"] = country
        # bank[account]["province"] = province
        # bank[account]["street"] = street
        # bank[account]["gate"] = gate
        # bank[account]["money"] = money
        # bank[account]["bank_name"] = bank_name
        pass
    pass


def login():
    print("执行操作前请输入账号和密码")
    while True:
        bank_zhanghao = input("账号：")
        bank_mima = input("密码：")
        if booleanuser(bank_zhanghao):
            if bank_zhanghao.isdigit():
                bank_zhanghao = int(bank_zhanghao)
                pass
            else:
                print("账号或密码输入错误请重新输入")
                islogin = input("是否继续登录：yes or no?")
                if islogin == "no":
                    break
                    pass
                else:
                    pass
            if bank_mima == selectuser(bank_zhanghao).password:
                global loginid
                loginid = 1
                return bank_zhanghao
                pass
            else:
                print("账号或密码输入错误请重新输入")
                islogin = input("是否继续登录：yes or no?")
                if islogin == "no":
                    break
                    pass
                else:
                    pass

        else:
            print("账号或密码输入错误请重新输入")
            islogin = input("是否继续登录：yes or no?")
            if islogin == "no":
                break
                pass
            else:
                pass


def quit():
    global loginid
    loginid = 0
    pass


# 取钱功能
def qv(bank_zhanghao):
    while True:
        qvqian = input("请输入您要取的金额：")
        qvqian = int(qvqian)
        if qvqian > selectuser(bank_zhanghao).money:
            print("不好意思您的钱不够，请重新输入金额")
            q = input("是否退出当前用户？yes or no？")
            if q == "yes":
                quit()
            pass
        else:
            user = selectuser(bank_zhanghao)
            user.money = selectuser(bank_zhanghao).money - qvqian
            saveorupd(user)
            print("系统正在加载", end="")
            for i in range(5):
                print(".", end="")
                time.sleep(1)
                pass
            print("取钱成功！")
            q = input("是否退出当前用户？yes or no？")
            if q == "yes":
                quit()
            break
            pass
    pass


# 存钱功能
def cun(bank_zhanghao):
    cunqian = int(input("请输入您要存储的金额："))
    user1 = selectuser(bank_zhanghao)
    qian = selectuser(bank_zhanghao).money + cunqian
    user1.money = qian
    saveorupd(user1)
    print("系统正在加载", end="")
    for i in range(5):
        print(".", end="")
        time.sleep(1)
        pass
    print("存储成功！")
    q = input("是否退出当前用户？yes or no？")
    if q == "yes":
        quit()
    pass


# 转账功能
def zhuanzhang(bank_zhanghao):
    zhuanid = 0
    while True:
        if zhuanid == 0:
            zhuanid = int(input("请输入您要转入的对方账号："))
            if not booleanuser(zhuanid):
                zhuanid = 0
                print("查无此账号！")
                continue
        zhuanqian = input("请输入您要转账的金额：")
        zhuanqian = int(zhuanqian)
        if zhuanqian > selectuser(bank_zhanghao).money:
            print("不好意思您的钱不够，请重新输入金额")
            q = input("是否退出当前用户？yes or no？")
            if q == "yes":
                quit()
            pass
        else:
            zhuaniduser = selectuser(zhuanid)
            bank_zhanghaouser = selectuser(bank_zhanghao)
            zhuaniduser.money = selectuser(zhuanid).money + zhuanqian
            bank_zhanghaouser.money = selectuser(bank_zhanghao).money - zhuanqian
            saveorupd(bank_zhanghaouser)
            saveorupd(zhuaniduser)
            print("系统正在加载", end="")
            for i in range(5):
                print(".", end="")
                time.sleep(1)
                pass
            print("转账成功！")
            q = input("是否退出当前用户？yes or no？")
            if q == "yes":
                quit()
            break
            pass
    pass


# 查询功能
def cha(bank_zhanghao):
    print("系统正在加载", end="")
    for i in range(5):
        print(".", end="")
        time.sleep(1)
        pass
    print("以下是您的个人信息：")
    info = '''
        ----------个人信息------
        用户名：%s
        地址信息
            国家：%s
            省份：%s
            街道：%s
            门牌号: %s
        余额：%s
        开户行地址：%s
        ------------------------
    '''
    user2 = selectuser(bank_zhanghao)
    print(info % (user2.username, user2.country, user2.province,
                  user2.street,
                  user2.door, user2.money, user2.bankname))
    q = input("是否退出当前用户？yes or no？")
    if q == "yes":
        quit()


if __name__ == '__main__':
    while True:

        # 打印欢迎程序
        welcome()
        chose = input("请输入您的业务：")
        if chose == "1":
            addUser()
        elif chose == "2":
            if loginid == 0:
                bank_zhanghao = login()
            if loginid == 1:
                cun(bank_zhanghao)
            else:
                print("请执行以下操作")
            pass
        elif chose == "3":
            if loginid == 0:
                bank_zhanghao = login()
            if loginid == 1:
                qv(bank_zhanghao)
            else:
                print("请执行以下操作")
            pass
        elif chose == "4":
            if loginid == 0:
                bank_zhanghao = login()
            if loginid == 1:
                zhuanzhang(bank_zhanghao)
            else:
                print("请执行以下操作")
            pass
        elif chose == "5":
            if loginid == 0:
                bank_zhanghao = login()
            if loginid == 1:
                cha(bank_zhanghao)
            else:
                print("请执行以下操作")
            pass
        elif chose == "6":
            loginid = 0
            print("欢迎下次光临！")
            # 6.关闭资源
            cursor.close()
            con.close()
            break
        else:
            print("输入错误！请重新输入！")








