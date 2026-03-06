class deneme6:
    def kayıt():
        sayılar=[]
        import os
        
        with open("kayıtlar.txt","r",encoding="utf-8")as f:
            for line in f:
                try:
                    sayı=int(line.strip())
                    sayılar.append(sayı)
                except ValueError:
                    continue

        sayılar.sort()

        with open("sonkayıt.txt","w",encoding="utf-8")as f:
            for sayı in sayılar:
                f.write(str(sayı))

        print("Kayıtlar sıralandı ve sonkayıt.txt dosyasına yazıldı.")

deneme6.kayıt()

        


 