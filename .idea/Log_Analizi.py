class Log_Analizi:
    
    import re
    
    def IP_bulma():
        log_verisi = """
        Hata: Kullanıcı 192.168.1.15 adresinden hatalı giriş yaptı.
        Sistem güncellendi. Sunucu ip: 10.0.0.1.
        Geçersiz deneme: 999.999.999.999 (Bu bir IP değil!)
        Bazı rakamlar: 12345, 1.2.3 (Bu da değil).
        Saldırı girişimi: 172.16.254.1 adresinden tespit edildi.
        """
        IP_şekil=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        IP_ler=re.findall(IP_şekil,log_verisi)


        for IP in IP_ler:
            parçalar=IP.split(".")
            if all(0<=int(parça)<=255 for parça in parçalar):
                print(f"Geçerli IP: {IP}")
            else:
                print(f"Geçersiz IP: {IP}")


    IP_bulma()
    

        


