class deneme9:
    def personel():
        import csv
        veriler=[
            ["isim","departman","maas"],
            ["Ahmet","yazılım",80000],
            ["Ayşe","pazarlama",65000],
            ["Mehmet","yazılım",95000],
            ["Zeynep","ık",70000],
            ["Can","yazılım",75000],
            ["Ece","pazarlama",60000]
        ]                          #newline satırlar arasında boşluk olmasın diye
        with open("personel.csv","w",newline="",encoding="utf-8") as f:
            yazici=csv.writer(f)
            yazici.writerows(veriler)

        yazılım_maas=[]

        with open("personel.csv","r",encoding="utf-8") as f:
            okuyucu=csv.DictReader(f)
            for line in okuyucu:
                if line["departman"]=="yazılım":
                    yazılım_maas.append(int(line["maas"]))


        if yazılım_maas:
            ortalama=sum(yazılım_maas)/len(yazılım_maas)
            print(f"Yazılım departmanındaki personelin ortalama maaşı: {ortalama:.2f} TL") 
        else:
            print("Yazılım departmanında personel bulunmamaktadır.")

deneme9.personel()