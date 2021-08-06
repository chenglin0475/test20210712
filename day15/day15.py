from collections import Counter
f = open(r"C:\Users\Administrator\Desktop\python\day15[文件读取]\任务\baidu_x_system.log",mode="r+",encoding="utf-8")
# list = []
# for i in f.readlines():
#     list.append(i.split(" ")[0])
list = [i[0] for i in [i.split(" ") for i in f.readlines()]]
print(Counter(list))
