class human:
    def __init__(self,age,sex,name):
        self.age = age
        self.sex = sex
        self.name = name
        pass
    pass

class gong(human):
    xingwei = ""
    pass

class student(human):
    xingwei = ""
    pass

g = gong(10,"男","突击队员")
g.xingwei = "干活"
print(g.name+"在"+g.xingwei)
s = student(70,"男","老牛")
s.xingwei = "学习，唱歌"
print(s.name+"在"+s.xingwei)

