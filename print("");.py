class Telefon_rehberi():
    def __init__(self):
        self.telefon_rehberı={}
  
    def rehber_ekle(self):
        numara=input("numara: ")
        if numara in self.telefon_rehberı:
            print("Bu numara zaten rehberde kayıtlı.")
        else:
            isim=input("isim: ")
            self.telefon_rehberı[numara]={"isim":isim}
            print("Kişi rehbere eklendi.")

    def rehber_listele(self):
        if not self.telefon_rehberı:
            print("Kayıtlı kişi yok.")
        else:
            for numara,isim in self.telefon_rehberı.items():
                print("numara: {}, isim: {}".format(numara,isim))

    def kisi_ara(self):       
        isim=input("İsim: ")  
        bulundu=False
        if isim in self.telefon_rehberı.items():
            for numara,isim_dict in self.telefon_rehberı.items():
                if isim_dict["isim"]==isim:
                    print("numara: {}, isim: {}".format(numara,isim))
                    bulundu=True
        else:
            print("Kayıtlı kişilerde bulunamadı.") 

    def rehber_sil(self):
        isim=input("isim: ")
        if isim in self.telefon_rehberı.values():
            for numara,isim_dict in list(self.telefon_rehberı.items()):
                if isim_dict["isim"]==isim:
                    del self.telefon_rehberı[numara]
                    print("Kişi rehberden silindi.")

        else:
            print("Kayıtlı kişilerde bulunamadı.")                     

    def islem_secimi(self):
        while True:
            print("1-Kişi ekle")
            print("2-Rehberi listele")
            print("3-Kişi ara")
            print("4-Kişi sil")
            print("5-Çıkış")

            secim=input("Seçiminiz(1-5): ")

            if secim=="1":
                self.rehber_ekle() 
            elif secim=="2":
                self.rehber_listele()
            elif secim=="3":
                self.kisi_ara()
            elif secim=="4":
                self.rehber_sil()
            elif secim=="5":
                print("çıkış yapılıyor")
                break
            else:
                print("Geçersiz seçim!")
                

if __name__=="__main__":
    rehber=Telefon_rehberi()
    rehber.islem_secimi()

 