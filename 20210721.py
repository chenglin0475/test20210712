'''
    中国工商银行账户管理系统：
        ICBC:
'''
import random

# 1.准备一个数据库 和 银行名称
import time

bank = {}  # 空的数据库
'''
    {
        "s001":{
            "张三":"张三",
            country:"中国"
        }，
        "s002":{

        }


    }

'''
bank_name = "中国工商银行昌平回龙观支行"  # 银行名称写死的

global loginid
loginid = 0
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
    # 1.判断数据库是狗已满
    if len(bank) >= 100:
        return 3
    # 2.判断用户是否存在
    if account in bank:
        return 2
    # 3.正常开户
    bank[account] = {
        "username": username,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "gate": gate,
        "money": money,
        "bank_name": bank_name
    }
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
    if account in bank:
        account = random.randint(10000000, 99999999)
    status = bank_addUser(account, username, password, country, province, street, gate, money)

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
        bank[account]["username"] = username
        bank[account]["password"] = password
        bank[account]["country"] = country
        bank[account]["province"] = province
        bank[account]["street"] = street
        bank[account]["gate"] = gate
        bank[account]["money"] = money
        bank[account]["bank_name"] = bank_name
        pass
    pass

def login():
    print("执行操作前请输入账号和密码")
    while True:
        bank_zhanghao = input("账号：")
        bank_mima = input("密码：")
        bank_zhanghao = int(bank_zhanghao)
        if bank_zhanghao in bank:
            if bank_mima == bank[bank_zhanghao]["password"]:
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
        if qvqian > bank[bank_zhanghao]["money"]:
            print("不好意思您的钱不够，请重新输入金额")
            q = input("是否退出当前用户？yes or no？")
            if q == "yes":
                quit()
            pass
        else:
            bank[bank_zhanghao]["money"] = bank[bank_zhanghao]["money"] - qvqian
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
    # while True:
    cunqian = int(input("请输入您要存储的金额："))
    qian =  bank[bank_zhanghao]["money"]+cunqian
    bank[bank_zhanghao]["money"] = qian
    print("系统正在加载", end="")
    for i in range(5):
        print(".", end="")
        time.sleep(1)
        pass
    print("存储成功！")
    q = input("是否退出当前用户？yes or no？")
    if q == "yes":
        quit()
    # break
    pass
# 转账功能
def zhuanzhang(bank_zhanghao):
    zhuanid = 0
    while True:
        if zhuanid ==0:
            zhuanid = int(input("请输入您要转入的对方账号："))
            if zhuanid not in bank :
                zhuanid = 0
                print("查无此账号！")
                continue
        zhuanqian = input("请输入您要转账的金额：")
        zhuanqian = int(zhuanqian)
        if zhuanqian > bank[bank_zhanghao]["money"]:
            print("不好意思您的钱不够，请重新输入金额")
            q = input("是否退出当前用户？yes or no？")
            if q == "yes":
                quit()
            pass
        else:
            bank[zhuanid]["money"] = bank[zhuanid]["money"] + zhuanqian
            bank[bank_zhanghao]["money"] = bank[bank_zhanghao]["money"] - zhuanqian
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
    print(info % (bank[bank_zhanghao]["username"], bank[bank_zhanghao]["country"], bank[bank_zhanghao]["province"], bank[bank_zhanghao]["street"],
                  bank[bank_zhanghao]["gate"], bank[bank_zhanghao]["money"], bank[bank_zhanghao]["bank_name"]))

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
        break
    else:
        print("输入错误！请重新输入！")








