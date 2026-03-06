class deneme5:
    
    def dosya():
        text="Ahmet,90\nAyşe,92\nMehmet,78\nZeynep,95\nCan,60"
        import os
        with open("ogrenciler.txt","w", encoding="utf-8") as f:
            f.write(text)

        basarılı=[]

        with open("ogrenciler.txt","r", encoding="utf-8") as f:
            for line in f:
                isim, notu=line.strip().split(" ,")
                if int(notu)>=80:
                    basarılı.append(isim)

        with open("basarılı.txt","w", encoding="utf-8") as f:
            for isim in basarılı:
                f.write(isim)

        print("Başarılı öğrenciler eklendi")
            
deneme5.dosya()
        

        
