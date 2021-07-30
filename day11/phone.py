class old:
    paizi = ""
    def setpaizi(self,paizi):
        self.paizi = paizi
        pass
    def getpaizi(self):
        return self.paizi
    def call(self,person):
        print("正在给"+ person + "打电话.....")
        pass
    pass

class new(old):
    # person = ""
    def call(self,person):
        super().call(person)
        print("语音拨号中...")

        pass
    def jieshao(self):
        print("品牌为：" + self.paizi + "很好用....")
        pass
    pass

huawei = new()
huawei.paizi = "华为"
huawei.call("企鹅")
huawei.jieshao()
