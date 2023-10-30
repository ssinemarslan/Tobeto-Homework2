#Mükemmel sayı bulan program
sayi=int(input("Lütfen sayı giriniz"))
carpantoplam=0
for i in range(1,sayi):
    if  sayi%i==0:
        carpantoplam+=i
        #carpantoplam=carpantoplam+i
if (carpantoplam==sayi):
    print("Sayı mükemmel sayıdır.")
else:
    print("Sayı mükemmel sayı değidir.")