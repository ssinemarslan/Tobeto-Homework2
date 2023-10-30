#asal çarpanlari bulan program
def findPrimeNumber(sayi):
    if(sayi > 1):
        for i in range(2,sayi):
            if(sayi % i == 0):
                break
        else:
            return sayi
        
sayi = int(input("sayı giriniz: "))
asalCarpan = []

for i in range(2,sayi+1):
    if(sayi % i == 0):
        if(findPrimeNumber(i) != None):
            asalCarpan.append(i)
print(f"Girilen sayının asal çarpanları: {asalCarpan}")
