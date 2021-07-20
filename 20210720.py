'''
    任务1：
        将导航系统与商城系统结合一起。
'''
import random
data = {
    "北京":{
        "昌平":{
            "十三陵":["十三陵水库","沙河水库"],
            "高校":["北京邮电大学","中央戏剧学院","北京师范大学","华北电力大学","北京航空航天大学"],
            "天通苑":["海底捞","呷哺呷哺"]
        },
        "海淀":{
            "公主坟":["军事博物馆","中华世纪园"],
            "科普场馆":["中国科技馆","北京天文馆"],
            "高校":["北京大学","清华大学"],
            "景区":["北京植物园","香山公园","玉渊潭公园"]
        },
        "朝阳":{
            "龙城":["鸟化石国家地质公园","朝阳南北塔"],
            "双塔":["朝阳凌河公园","朝阳凤凰山"]
        },
        "延庆":{
            "龙庆峡":["龙庆峡景区"]
        }
    }
}

# 打印城市
def print_place(choice):
    for i in choice:
        print(i)

# 攻略
for i in data:
    print(i)


def shopping(dizhi):
    # 1.准备商品
    shop = [
        ["劳力士手表", 200000],
        ["Iphone 12X plus", 12000],
        ["lenovo PC", 6000],
        ["HUA WEI WATCH", 1200],
        ["Mac PC", 15000],
        ["辣条", 2.5],
        ["老干妈", 13]
    ]
    print("欢迎来到",dizhi,"的购物商场")
    # 2. 初始化钱包
    money = input("请输入您的余额：")
    while not money.isdigit():
        money = input("输入错误请您重新输入您的余额：")
        money = int(money)  # "200000" --> 200000
        pass
    money = int(money)
    quan = 0;
    # 3.空的购物车
    mycart = []
    j = 0
    print("温馨提示：是否要抽取一张优惠券？yes or no")
    while (j < 1):
        you = input()
        if you == "yes":
            num = random.randint(0, 30)
            if num <= 10:
                print("恭喜您，抽到老干妈7折优惠券！")
                quan = quan + 1;
                j = j + 1
                pass
            else:
                print("恭喜您，抽到联想电脑1折优惠券！")
                quan = quan + 2;
                j = j + 1
                pass
            pass
        elif you == "no":
            j = j + 1
            pass
        else:
            print("请输入正确指令！")
    # 4.买东西
    i = 0
    huaxiao = 0
    while i <= 20:
        # 4.1 展示商品
        for key, value in enumerate(shop):
            print(key, value)
        # 4.2 请输入您想要的商品
        chose = input("亲输入您想要的商品编号：")  # "1"
        # 4.3
        if chose.isdigit():
            chose = int(chose)
            # 4.4 先判断是否存在该商品
            if chose > 6:
                print("您输入的商品不存在！别瞎弄！")
            else:
                # 4.5 判断您的余额是否足够
                if money < shop[chose][1]:
                    print("对不起，穷鬼，您的钱不够！请到其他超市买东西去！")
                else:
                    if chose == 6 and quan == 1:
                        mycart.append(shop[chose])
                        huaxiao = shop[chose][1] * 0.7
                        money = money - huaxiao
                        mycart[len(mycart)-1][1] = huaxiao
                        quan = 0
                        pass
                    elif chose == 2 and quan == 2:
                        mycart.append(shop[chose])
                        huaxiao = shop[chose][1] * 0.1
                        money = money - huaxiao
                        mycart[len(mycart)-1][1] = huaxiao
                        quan = 0
                        pass
                    else:
                        # 4.6 将商品添加到购物车 ，余额减去对应的钱
                        mycart.append(shop[chose])
                        money = money - shop[chose][1]
                    print("恭喜，成功添加购物车！您的余额还剩￥：", money)
        elif chose == "q" or chose == "Q":
            print("拜拜了，您嘞！欢迎下次光临！")
            break
        else:
            print("对不起，您输入有误，请重新输入！")
        i = i + 1

    # 打印购物小条
    print("以下是您的购物小条，请拿好：")
    for key, value in enumerate(mycart):
        print(key, value)
    print("本次余额还剩：￥", money)
    pass

while True:
    city1 = input("请输入您要去的城市：")
    if city1 in data:
        print_place(data[city1])
        city2 = input("亲输入二级城市：")
        if city2 in data[city1]:
            print_place(data[city1][city2])
            city3  = input("亲输入三级地区：")
            if city3 in data[city1][city2]:
                print_place(data[city1][city2][city3])
                dizhi = input("请输入您要去的地方：")
                if dizhi in data[city1][city2][city3]:
                    print("欢迎来到",dizhi)
                    s = input("请问您是否要去购物商场？yes or no?")
                    if s == "yes":
                        # 商城系统
                        shopping(dizhi)
                        pass
                    else:
                        print("那您好好游玩不要乱跑")
                else:
                    print("在",data[city1][city2][city3],"地区没有你说的叫",dizhi,"的地方")

        else:
            print("当前二级城市不存在，别瞎弄！")
    elif city1 == 'q' or city1 == "Q":
        print("------------------欢迎下次光临Jason旅行社！------------------")
        break
    else:
        print("当前城市不存在，别瞎弄！")































