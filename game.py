'''
    猜数字游戏：
        需求：
            1.系统产生一个随机数，
            2.用户从键盘输入数据，与随机数进行比对
                2.1 若大了，温馨提示：大了
                2.2 若小了，提示：小了
                2.3 提示：恭喜您，猜中！

        技术选型：
            1.随机数技术
                import random
                random.randint(开始数据，结束数据)
            2.键盘输入技术
                name = input()
            3.判断技术：多分支判断
                if....else
                if...elif.....elif....else
            4.循环技术
                while 条件：
    任务：
        加上金币赌博功能。
            初始化有2000金币，没猜错一次，扣200金币。
            10机会，钱扣完为止。
            在机会过程中，若猜中，奖励5000金币。
            然后询问，是否继续？是，否。
'''
import random
# 1. 让系统产生一个随机数
count = 0
# 2.循环的让用户去猜
j = 0
jinbi = 2000
while j <1:
    i = 1
    data = random.randint(0, 200)
    print("开始新游戏：1")
    print("退出游戏：2")
    print("充值1000金币：3")
    print("现有金币：",jinbi)
    print("游戏规则：在五次内猜中一个随机的0~200之内的数字，每猜错一次扣200金币，猜对奖励1000金币")
    xuanxiang = input("请输入数字选项")
    xuanxiang = int(xuanxiang)
    if xuanxiang == 1:
        if jinbi <= 0:
            print("金币不够请充值")
        # while i <= 5:
        while jinbi >=200:
            count = count + 1
            num = input("请输入您要猜的数字：")# "22"   "23"
            num = int(num) # "22"  -->  22
            if num > data:
                if jinbi>=200:
                    jinbi = jinbi - 200
                else:
                    break
                print("大了！ 剩余金币：",jinbi)
            elif num < data:
                if jinbi >= 200:
                    jinbi = jinbi - 200
                else:
                    break
                print("小了！ 剩余金币：",jinbi)
            else:
                jinbi = jinbi + 1000
                print("恭喜，猜中了！本次幸运数字为：",data,"，本次猜了",count,"次！")
                break  # 终止循环
            # i = i + 1
        if i >= 6 or jinbi <= 0:
            print("游戏失败! 正确数字为：",data)
    elif xuanxiang == 2:
        j = j + 1
    elif xuanxiang ==3:
        jinbi = jinbi + 1000
    else:
        print("请输入正确选项")



















