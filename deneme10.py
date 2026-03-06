class deneme10:
    def hesapMakinesi():

        try:
            sayı1=int(input("enter"))
            sayı2=int(input("enter"))
            islem=sayı1/sayı2

        except ZeroDivisionError:
            print("sayı sıfıra bölünemez")
        except ValueError:
            print("lütfen sayı giriniz")
        except Exception as e:
            print("hata oluştu",e)

        finally:
            print("işlem tamamlandı")

deneme10.hesapMakinesi()


