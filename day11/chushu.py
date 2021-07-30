class chuzi:
    age = 0
    name = ""
    def setage(self,age):
        self.age = age
        pass
    def getage(self):
        return self.age
    def setname(self,name):
        self.name = name
        pass
    def getname(self):
        return self.name
    def zhufan(self):
        print("煮饭....")
        pass
    pass

class chuson(chuzi):
    def chao(self):
        print("炒菜....")
        pass
    pass
class chusonson(chuson):
    def zhufan(self):
        print("煮饭")
        pass
    def chao(self):
        print("炒菜")
        pass
chu = chusonson()
chu.age = 7
chu.name = "小孩"
print(chu.getage(),chu.getname())
chu.chao()
chu.zhufan()