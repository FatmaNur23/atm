class Deneme:
    def sayıBul():
        sayı=int(input("Enter:"))

        try:
            if sayı%2==0:
                print("Sayı çift")
            elif sayı%2==1:
                print("Sayı tek")
        except ValueError:
            print("Geçrsiz giriş")

    sayıBul()

