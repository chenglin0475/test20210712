from threading import Thread
import time


baozi = 0
class chuzi(Thread):
    name = ""
    makbao = 0
    def run(self) -> None:
        global baozi
        while True:
            if baozi <= 600:
                baozi += 1
                self.makbao += 1
                print(self.name,"正在做包子")
                time.sleep(0.5)
                pass
            else:
                print("篮子满了")
                print(self.name, "做了", self.makbao, "个包子\n")
                #break
                time.sleep(0.5)
                pass
            pass
        pass
class guke(Thread):
    gname = ""
    zijin = 3000
    maibao = 0
    def run(self) -> None:
        global baozi
        while True:
            if baozi > 0 and self.zijin>0:
                baozi -=1
                self.zijin -=2
                self.maibao +=1
                print(self.gname, "正买包子")
                pass
            elif baozi == 0:
                print("篮子空了")
                time.sleep(1)
                pass
            else:
                print(self.gname,"想买包子但是他没钱了")
                print(self.gname, "买了", self.maibao, "个包子\n")
                break
            pass
        pass

c1 = chuzi()
c2 = chuzi()
c3 = chuzi()
c1.name = "1号厨子"
c2.name = "2号厨子"
c3.name = "3号厨子"
g1 = guke()
g2 = guke()
g3 = guke()
g4 = guke()
g5 = guke()
g6 = guke()
g1.gname = "一号顾客"
g2.gname = "二号顾客"
g3.gname = "三号顾客"
g4.gname = "四号顾客"
g5.gname = "五号顾客"
g6.gname = "六号顾客"
c1.start()
c2.start()
c3.start()
g1.start()
g2.start()
g3.start()
g4.start()
g5.start()
g6.start()





