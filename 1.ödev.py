# -*- coding: utf-8 -*-

#Kullanıcıdan dik kenarları istenen üçgenin alan hesabı
a=int(input("Bir sayı girer misiniz? "))
b=int(input("Lütfen bir sayı daha girer misiniz? "))
print("Üçgenin Alanı: ",a*b/2)

#Kullanıcı'dan iki tane girdi alın ve bunların değerlerini değiştirin
m=int(input("M'nin değerini girer misin ? "))
n=int(input("N'nin değerini girer misin ? "))
print("M: ",n,"N: ",m)

#Harf Notu Hesabı
vn=int(input("Öğrencinin vize notunu giriniz: "))
pn=int(input("Öğrencinin proje notunu giriniz: "))
fn=int(input("Öğrencinin final notunu giriniz: "))
harfnotu=(vn*30/100)+(pn*20/100)+(pn*50/100)
print("Harf notu için hesaplanan puan: ",harfnotu)

if(80<harfnotu<=95):
    print("Tebrikler AA")
elif(75<harfnotu<=80):
    print("BB")
elif(70<harfnotu<=75):
        print("BC")
elif(60<harfnotu<=70):
    print("CC")
elif(50<harfnotu<=60):
    print("DC")
elif(45<harfnotu<=50):  
    print("DD") 
elif(25<harfnotu<=45):     
    print("FD")
else:
    print("FF")