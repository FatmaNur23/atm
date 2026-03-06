class deneme8:
    def kütüphane():
        kitaplar=[
            {"ad":"Nutuk","yazar":"Atatürk","sayfa":543},
            {"ad":"Simyacı","yazar":"Paulo Coelho","sayfa":184},
            {"ad":"1984","yazar":"George Orwell","sayfa":352}
        ]
        import json
        with open("kutuphane.json","w",encoding="utf-8") as f:
            json.dump(kitaplar, f,ensure_ascii=False, indent=4)

        yeni={"ad":"Suç ve ceza","yazar":"Dostoyevski","sayfa":687}

        with open("kutuphane.json","r",encoding="utf-8") as f:
            kutup_python=json.load(f)
            kutup_python.append(yeni)

        with open("kutuphane.json","w",encoding="utf-8") as f:
            json.dump(kutup_python, f,ensure_ascii=False, indent=4)

            
        


        

            
 


 
 
