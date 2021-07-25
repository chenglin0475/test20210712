'''
chenlgin
20210723

    每个月的销售总金额：
    全年的销售总额：
    每种衣服的销售总额：
    每个季度销售总额占比：
    全年每种销售数量占比：
'''
import  xlrd
wd = xlrd.open_workbook("2020年每个月的销售情况.xlsx",encoding_override=True)
yue = ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]
#每月销售总额字典
meiYueXiaoShou = {}
#没中衣服销售总额字典
meiZhongYiFu = {}
#每个季度销售额
jiduzb = {}
#每种销售总额占比
mzzb = {}
#计算每个月销售总额的方法
def meiGeYue():
    for i in yue:
        st = wd.sheet_by_name(i)
        rows = st.nrows
        cols = st.ncols
        sum = 0
        for j in range(1,rows):
            danJia = float(st.cell_value(j,2))
            xiaoLiang = float(st.cell_value(j,4))
            xiaoShouE = danJia * xiaoLiang * rows
            sum = sum + xiaoShouE
            pass
        meiYueXiaoShou[i] = sum
        pass
    pass
#计算全年销售总额的方法
def quanNian():
    meiGeYue()
    sum = 0
    for i in yue:
        sum = sum + float(meiYueXiaoShou[i])
        pass
    return sum
#每种衣服的销售总额
def yfXiaoShou():
    for i in yue:
        st = wd.sheet_by_name(i)
        rows = st.nrows
        cols = st.ncols
        sum = 0
        for j in range(1,rows):
            yf = st.cell_value(j, 1)
            danJia = float(st.cell_value(j,2))
            xiaoLiang = float(st.cell_value(j,4))
            if yf not in meiZhongYiFu:
                meiZhongYiFu[yf] = 0
                pass
            sum = meiZhongYiFu[yf]
            xiaoShouE = danJia * xiaoLiang * rows
            meiZhongYiFu[yf] = sum + xiaoShouE
            pass
        pass
    pass
meiGeYue()
yfXiaoShou()
#每个季度销售总额占比
def jiDu():
    quanNian()
    jiduzb["春季占比"] = 0
    jiduzb["夏季占比"] = 0
    jiduzb["秋季占比"] = 0
    jiduzb["冬季占比"] = 0
    c = 0
    x = 0
    q = 0
    d = 0
    for i in yue:
        j = float(meiYueXiaoShou[i])
        if i == "12月" or i == "1月" or i == "2月":
            d = d + 1
            jiduzb["冬季占比"] = jiduzb["冬季占比"] + j
            if d == 3:
                jiduzb["冬季占比"] = jiduzb["冬季占比"] / quanNian()
                pass
            pass
        if i == "3月" or i == "4月" or i == "5月":
            c = c + 1
            jiduzb["春季占比"] = jiduzb["春季占比"] + j
            if c == 3:
                jiduzb["春季占比"] = jiduzb["春季占比"] / quanNian()
                pass
            pass
        if i == "6月" or i == "7月" or i == "8月":
            x = x + 1
            jiduzb["夏季占比"] = jiduzb["夏季占比"] + j
            if x == 3:
                jiduzb["夏季占比"] = jiduzb["夏季占比"] / quanNian()
                pass
            pass
        if i == "9月" or i == "10月" or i == "11月":
            q = q + 1
            jiduzb["秋季占比"] = jiduzb["秋季占比"] + j
            if q == 3:
                jiduzb["秋季占比"] = jiduzb["秋季占比"] / quanNian()
                pass
            pass
jiDu()
#全年每种销售占比
def meizzb():
    for i in meiZhongYiFu:
        mzzb[i] = meiZhongYiFu[i] / quanNian()
        pass
    pass

meizzb()


print("每个月销售总额：",meiYueXiaoShou)
print("全年销售总额：",quanNian())
print("每件衣服的销售总量：",meiZhongYiFu)
print("每个季度占总销售额的占比：",jiduzb)
print("每种衣服占总额比：",mzzb)





