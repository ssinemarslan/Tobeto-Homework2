#Asal sayı kontrol programı
sayi=int(input("Lütfen bir sayi giriniz"))
if sayi>1:

    for i in range(2,sayi):
        if (sayi%i)==0:
            print(sayi,"Asal sayı değildir.")
            break
    else:
        print(sayi,"Sayı asaldır")

else:
    print(sayi,"Asal sayı değildir.")

