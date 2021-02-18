#Kod açıklanmıştır, hem fonksiyon kullanmadan hemde fonksiyon kullanarak sonuç bulunmuştur.
'''
SORU:
Generating a 3x3 matrix with 9 random prime numbers. (You have to do it using the for loop.)
9 rastgele asal sayı ile 3x3 matris oluşturma. (Bunu for döngüsünü kullanarak yapmanız gerekir.)'''

import random as rnd # random sayı üretebilmek için random kütüphanesi import edildi

'''
FONKSİYON KULLANMADAN BULUNAN SONUÇ 
KODUN AÇIKLAMASI:
3x3'lük matriste 1-10 arası rastgele sayı üretilir. Üretilen sayının asal olup olmadığı bilenemediği için 
While döngüsü sonsuz döngü olarak kullanılır. Kodda sayının 1'den büyük olma durumuna bakılır. 
Sayı 1'den büyük ise bir for döngüsü ile en küçük asal sayı 2 oldugu için 2'den sayıya kadar olan(uretilen sayı dahil 
değil) tüm sayıların moduna(kalanına) bakar. Aralıktaki herhangi bir rakamın (k) kalanı 0 olursa rastgele üretilen sayı
asal değildir, döngüden break ile çıkılır. for içerisindeki if koşulu hiçbir zaman sağlanmazsa üretilen sayi asaldır,
bu durumda number ekrana yazdırılır.
'''

print("FONKSİYON KULLANMADAN BULUNAN ASAL SAYILAR MATRİSİ")
for i in range(0,3):
    print("\n")
    for j in range(0,3):
        while True:
            number=rnd.randint(1, 10) #1-10 arası int veri türünde rastgele sayı üretilir.
            if number>1:  #eğer number 1'den büyük ise
                for k in range(2,number): # 2'den number-1'e kadar devam eden döngüye girer
                    if(number%k)==0: # number değişkeninin herhangi bir sayı(i değerine) ile bölümünden kalan 0 ise sayı asal değildir
                        break # asal olmama durumudur, döngüyü kırar ve döngüden çıkar.
                else:
                    print(number,end="\t")# number değişkeni, 1 ve kendisinden başka herhangi bir sayıya bölünmüyorsa sonucu ekrana yazdırır.
                    break # while ile oluşturulan sonsuz döngüyü kırar.

''' 
FONKSİYON İLE BULUNAN SONUÇ 
KODUN AÇIKLAMASI:
3x3'lük matriste 1-10 arası rastgele sayı üretilir. Üretilen sayının asal olup olmadığı bilenemediği için 
While döngüsü sonsuz döngü olarak kullanılır. asalmi fonksiyonunun cevabı True ise sayı asaldır ve 
matris formunda ekrana yazdırılır.

asalmi Fonksiyonu İşleyişi: Rastgele üretilen sayının asal olup olmadığını bulan fonksiyon main'de rastgele üretilen 
sayıyı parametre olarak alır. İlk olarak sayının 1'den büyük olma durumuna bakılır. 
Sayı 1'den büyük değilse False değerini döndürür. Sayı 1'den büyük ise bir for döngüsü ile en küçük asal sayı 2 oldugu 
için 2'den sayıya kadar olan(uretilen sayı dahil değil) tüm sayıların moduna(kalanına) bakar. 
Aralıktaki herhangi bir rakamın (i) kalanı 0 olursa rastgele üretilen sayı asal değildir, 
fonksiyon False değerini döndürür. for içerisindeki if koşulu hiçbir zaman sağlanmazsa üretilen sayi asaldır 
ve fonksiyon True değerini döndürür.
'''


def asalmi(number):  
    if number > 1: #eğer sayı 1'den büyük ise
        for i in range(2,number): # 2'den number-1'e kadar devam eden döngüye girer
            if (number % i) == 0: # number değişkeninin herhangi bir sayı(i değerine) ile bölümünden kalan 0 ise sayı asal değildir
                return False # asal olmama durumudur, fonksiyon False değerini döndürür    
        return True # asal olma durumudur, fonksiyon True değerini döndürür    
    return False
 
print("\nFONKSİYON İLE BULUNAN ASAL SAYILAR MATRİSİ")
for i in range(0,3):
    print("\n")
    for j in range(0,3):
        while True:
            number=rnd.randint(1, 10) #1-10 arası int veri türünde rastgele sayı üretilir.
            if(asalmi(number)==True): # eğer asalmi fonksiyonundan dönen değer True ise sayı asaldır ve sayı ekrana yazdırılır 
                print(number,end="\t")
                break # while ile oluşturulan sonsuz döngüyü kırar.
