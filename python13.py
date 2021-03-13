

"""
Fonksiyonlar islerimizi oldukca kolaylastiriyor.Ornegin bir personel listemiz olsun,
bu personel listesinde yeni gelen personeller olabilir,ya da personellerin bilgilerini degistirip yenilemek
isteyebiliriz.Bunun icin her seferinde print() fonskiyonu kullanmak hata yapmamizi kolaylastircak ve islerimiz
zorlasacaktir.Bunun yerine bir fonksiyon tanimlariz istedigimiz bilgileri guncelleyebiliriz,yeni bilgiler ekleyebiliriz.
"""
#Hepimiz belli hesaplara giris yapiyoruz ve karsimiza "MERHABA ismimiz" yazisi cikiyordur..
#Peki bu nasil oluyor? Hepimize ozel olmadigini biliyoruz :)))))))))))))

def karsilama(isim):                #fonksiyon tanimi
    print(f"MERHABA {isim}")

karsilama("Tugba")                  #fonksiyon cagrisi

def karsilama2():
    isim=input("İsminiz:")
    print("Merhaba "+isim+ " SISTEME HOS GELDINIZ!")

karsilama2()
#Bir fonksiyon cagrilmadan asla calismaz..

#Bir personel listesi olusturalim,yeni personeller ekleyelim..

def personel_ekle(ad,soyad,sehir,yas,tel_no):  #Fonksiyonu tanimladik..

    print("*"*20)

    print("AD :",ad)
    print("SOYAD :",soyad)
    print("SEHİR :",sehir)
    print("YAS :",yas)
    print("TELEFON :",tel_no)

    print("*"*20)
    
personel_ekle("Sila","Nur","Kayseri",20,"05001221654")          #Fonskiyonu cagirdik..
personel_ekle("Can","Huseyin","Ankara",24,"05103546512")         #istedigimiz kadar personel ekleyebiliriz..


#python da len fonksiyonu olmasaydi ne olurdu?
#kendi len fonksiyonumuzu olustururduk..Peki nasil?

def Mylen(oge):
    i=0
    for bul in oge:
        i+=1   
    print("Girdiginiz ogenin uzunlugu:{}".format(i))       #burada print yerine de dikkat etmek gerekiyor.
                                                           #print fonk. icinde fakat for icinde degil.
Mylen("Tugba")                                             #for icinde olsaydi her harf de uzunluk yazacakti..
Mylen(["Tugba",5,"Kirac"])                                 #Liste uzunlugunu da verdi.
Mylen({"Tugba":"Kirac",5:"Can"})                           #Sozluk uzunlugunu da verdi..
