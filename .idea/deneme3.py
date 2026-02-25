class deneme3:
    def atm(self): 
        dogru_sifre="2023"
        deneme=3
        while deneme>0:
            şifre=input("şifre:")
            
            if şifre==dogru_sifre:
                print("sisteme girebilirsiniz")
                break
            else:
                deneme-=1
                print(f"yanlış şifre, kalan deneme: {deneme}")
            
            if deneme==0:
                print("hesabınız bloke olmuştur")
                return


        bakiye=1000
        işlem_geçmişi=[] 

        while True:
            secim=int(input("1-bakiye görüntüle\n2-para yatır\n3-para çek\n4-çıkış\nSeçiminiz:"))
            
            if secim==1:
                print(f"Bakiye:{bakiye}")
                işlem_geçmişi.append("Bakiye görüntülendi")
            elif secim==2:
                try:
                    miktar=int(input("Yatırmak istediğiniz miktar:"))
                    if miktar >0:
                        bakiye+=miktar
                        print(f"Bakiye:{bakiye}")
                        işlem_geçmişi.append(f"Para yatırıldı: {miktar}")
                except ValueError:
                    print("Lütfen geçerli bir miktar girin.")  
            elif secim==3:
                try:
                    miktar=int(input("Çekmek istediğiniz miktar:"))
                    if miktar >0 and miktar <= bakiye:
                        bakiye-=miktar
                        print(f"Bakiye:{bakiye}")
                        işlem_geçmişi.append(f"Para çekildi: {miktar}")
                except ValueError:
                    print("Lütfen geçerli bir miktar girin.")
            elif secim==4:
                break

        print("İşlem Geçmişi:")
        for işlem in işlem_geçmişi:
            print(işlem)
obj=deneme3()
obj.atm()

   


