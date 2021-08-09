
f = open(r"test5.txt",mode="r+",encoding="utf-8")
f1 = open(r"D:\\魔法成绩.txt",mode="w+",encoding="utf-8")
for i in [i.split(" ") for i in f.readlines()]:
    a = 0
    for j in range(1,len(i)):
        a = a + int(i[j])
        pass

    f1.write(i[0]+":"+str(a))
    f1.flush()
    pass

f.close()
f1.close()






