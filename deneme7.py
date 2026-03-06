class deneme7:
    def sat():
        dict={
            "Elma:20",
            "Armut:30",
            "Elma:20",
            "Çilek:50",
            "Armut:30",
            "Elma:20"
        }
        rapor={}
        import os
        with open("satıslar.txt","w",encoding="utf-8") as f:
            for meyve,fiyat in dict.items():
                f.write(f"{meyve}:{fiyat}")

        with open("satıslar.txt","r",encoding="utf-8") as f:
            for line in f:
                meyve,fiyat=line.strip().split(":")
                if meyve in rapor:
                    rapor[meyve]+=int(fiyat)
                else:
                    rapor[meyve]=int(fiyat)

        with open("rapor.txt","w",encoding="utf-8")as f:
            for meyve,fiyat in rapor.items():
                f.write(f"{meyve}:{fiyat}\n")
        
      

