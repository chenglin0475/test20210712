

def shanc(name,str):
    f = open(r""+str+"",mode="rb")
    f1 = open(r"D:\\"+name+".png",mode="wb")
    data = f.read()
    f1.write(data)
    f1.flush()
    f.close()
    f1.close()


