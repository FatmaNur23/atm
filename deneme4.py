class deneme4:
    from collections import Counter
    
    def kelime_sayacı():
        metin=input("Enter:")
        yenimetin=metin.lower()
        kelimeler=yenimetin.split()
        
        sayac=Counter(kelimeler)

        return sayac.most_common(3)
    sonuç=kelime_sayacı()
    print(sonuç)

class deneme42:
    def anagram_grup(kelimeler):
        anagramlar={}

        for kelime in kelimeler:
            yenikelime="".join(sorted(kelime))
            if yenikelime in anagramlar:
                anagramlar[yenikelime].append(kelime)
            else:
                anagramlar[yenikelime]=[kelime]

        return list(anagramlar.values())

    list=["aks","kas","elma","amel"]
    print(anagram_grup(list))





        
        
         

    

        
        
 