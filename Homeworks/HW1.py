# Kod açıklanmıştır, hem fonksiyon kullanmadan hemde fonksiyon kullanarak sonuç bulunmuştur.
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
bu durumda sayi ekrana yazdırılır.
'''
for i in range(0,3):
    print("\n")
    for j in range(0,3):
        while True:
            sayi=rnd.randint(1, 10)
            if sayi>1:
                for k in range(2,sayi):
                    if(sayi%k)==0:
                        break # asal olmama durumu
                else:
                    print(sayi,end=" ")
                    break

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

'''
def asalmi(sayi):  
    if sayi > 1:
        for i in range(2,sayi):
            if (sayi % i) == 0:
                return False #asal degil           
        return True #asal
    return False
 

for i in range(3):
    print("\n")
    for j in range(3):
        while True:
            sayi=random.randint(1, 10)
            if(asalmi(sayi)==True):
                print(sayi,end=" ")
                break
'''