class deneme2:
    def bulma():
        nums=[]
        toplam=0

        while True:
            num=input("enter:")

            if num=="q":
                break
            try:
                num=int(num)
                nums.append(num)
                toplam+=num
            except ValueError:
                print("geçersiz giriş")

        ort=toplam/len(nums) if nums else 0
        sayı=len(nums)
        byk=max(nums)
        kçk=min(nums)


        print(f"Toplam: {toplam}, Ortalama: {ort}, Sayı: {sayı}")
    bulma()

  
   