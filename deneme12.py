class kitap():
    def __init__(self,isim,yazar,sayfa):
        self.isim=isim
        self.yazar=yazar
        self.sayfa=sayfa

    def bilgi_göster(self):
        print(f"kitap adı: {self.isim}, yazar: {self.yazar}, sayfa sayısı: {self.sayfa}")

    
class kütüphane:
    def __init__(self):
        self.kitap_listesi=[]
    
    import json

    def kitap_ekle(self, kitap):
        self.kitap_listesi.append(kitap)

    def dosyaya_kaydet(self):
        kayıtlar=[]
        for k in self.kitap_listesi:
            kayıtlar.append({
                "isim": k.isim,
                "yazar": k.yazar,
                "sayfa": k.sayfa
            })
        with open("kutuphane.json","w",encoding="utf-8") as f:
            json.dump(kayıtlar,f,ensure_ascii=False,indent=4)

    def verileri_yükle(self):
        try:
            with open("kutuphane.json","r",encoding="utf-8") as f:
                veriler=json.load(f)
                for v in veriler:
                    yeni_kitap=kitap(v["isim"],v["yazar"],v["sayfa"])
                    self.kitap_listesi.append(yeni_kitap)
        except FileNotFoundError:
            return []
 
    

kütüphane1=kütüphane()
kütüphane1.verileri_yükle()

kitap1=kitap("harry potter","rowling",450)
kütüphane1.kitap_ekle(kitap1)
kütüphane1.dosyaya_kaydet()

for k in kütüphane1.kitap_listesi:
    k.bilgi_göster()
    