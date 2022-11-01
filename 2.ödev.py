# -*- coding: utf-8 -*-

class Hayvan():
    def __init__(self,isim,tür,ayaksayısı,ses):
        self.isim=isim
        self.tür=tür
        self.ayaksayısı=ayaksayısı
        self.ses=ses 
    def özellikler(self):
        print("""
              Hayvanların Özellikleri:
                  
              İsmi: {}
              
              Türü: {}
              
              Ayak Sayısı: {}
              
              Sesi: {}
                      
             """.format(self.isim,self.tür,self.ayaksayısı,self.ses))
            
        
class Köpek(Hayvan):
 def ayaksayı(self,gidenayaksayı):
         print("Bir ayağı sakatlandığı için artık 3 ayaklı") 
         self.ayaksayısı -= gidenayaksayı
       
köpek1=Köpek("Dalmaçyalı Köpek", "Memeli",4,"havhav")
köpek1.özellikler()
köpek1.ayaksayı(1)

class Kuş(Hayvan):
 def ayaksayı(self,gidenayaksayı):
         print("Bir ayağı sakatlandığı için artık 1 ayaklı") 
         self.ayaksayısı -= gidenayaksayı
       
kuş1=Kuş(" Kanarya Kuşu", "Omurgalı",2,"cikcik")
kuş1.özellikler()
kuş1.ayaksayı(1)

class At(Hayvan):
 def ayaksayı(self,gidenayaksayı):
         print("İki ayağı sakatlandığı için artık 2 ayaklı") 
         self.ayaksayısı -= gidenayaksayı
       
at1=At(" İran Atı", "Memeli",4,"kişner")
at1.özellikler()
at1.ayaksayı(2)


        