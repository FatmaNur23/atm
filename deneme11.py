class bankahesabı:
    def __init__(self,hesapsahibi,bakiye=0):
        self.hesapsahibi=hesapsahibi
        self.bakıye=bakiye

    def parayatır(self,miktar):
        self.bakıye+=miktar
        print("bakıye",self.bakıye)

    def paracek(self,miktar):
        if self.bakıye>=miktar:
            self.bakıye-=miktar
        else:
            print("yetersiz bakiye")
        print("bakıye",self.bakıye)

    def bakıyesorgula(self):
        print("bakıye",self.bakıye)

    def bilgiyazdır(self):
        print(f"standart hesap: {self.hesapsahibi}")

hesap=bankahesabı("fatma",0)
hesap.parayatır(1000)
hesap.paracek(500) 
hesap.bakıyesorgula()
 
class vadelihesap(bankahesabı):
    def __init__(self,hesapsahibi,bakıye,faizoranı=0.05):
        super().__init__(hesapsahibi,bakıye)
        self.faizoranı=faizoranı

    def faizekle(self):
        yenibakiye=self.bakıye*self.faizoranı
        self.bakıye+=yenibakiye
        print("yeni bakiye",self.bakıye)

    def bilgiyazdır(self):
        print(f"vadeli hesap (faiz: {self.faizoranı}): {self.hesapsahibi}")

hesap=vadelihesap("fatma",1000)
hesap.faizekle() 
