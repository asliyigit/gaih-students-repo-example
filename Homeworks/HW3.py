#Kod açıklanmıştır

'''
SORU:
İki fonksiyon yazın.
İlk fonksiyonun adı prime_first.
İkinci fonksiyonun adı prime_second.
Bu iki fonksiyonu for döngüsünün içinde kullanmalısınız. For döngüsünün 0-1000 arasında değerler aldığından emin olun.
Prime_first fonksiyonları ile ekranda 0-500 arasındaki asal sayılara basın. 
Prime_second fonksiyonları ile ekranda 500-1000 arası asal sayılara basın.
'''


def prime_first(number): # prime_first fonksiyonu, 0-500 arasında olan ve parametre olarak gönderilen sayının asal sayı olup olmadığını bulur
	if number > 1:   #if number 1'den büyük ise
		for i in range(2,number):  # 2'den number-1'e kadar devam eden döngüye girer 
			if (number % i) == 0:  # number değişkeninin herhangi bir sayı(i değerine) ile bölümünden kalan 0 ise sayı asal değildir, 
				break  #döngüyü kırar ve döngüden çıkar.
		else:  
			print(number) # number 1 ve kendisinden başka herhangi bir sayıya bölünmüyorsa sonucu ekrana yazdırır.


def prime_second(number): # second fonksiyonu, 500-1000 arasında olan ve parametre olarak gönderilen sayının asal sayı 
	#olup olmadığını bulur
	if number > 1:   #if number 1'den büyük ise
		for i in range(2,number):   # 2'den number-1'e kadar devam eden döngüye girer 
			if (number % i) == 0:   # number değişkeninin herhangi bir sayı(i değerine) ile bölümünden kalan 0 ise sayı asal değildir
				break  #döngüyü kırar ve döngüden çıkar.
		else:  
			print(number) # number değişkeni, 1 ve kendisinden başka herhangi bir sayıya bölünmüyorsa sonucu ekrana yazdırır.

'''
Soruda istenen 0-1000 arasında olan for döngüsü yazıldı. Eğer number 0-500 arasında ise prime_first fonksiyonunu çağırır.
number 501-1000 arasında ise prime_second  fonksiyonunu çağırır ve sayının asal sayı olup olmadığının kontrolü yapılır
Asal sayılar prime_first ve prime_second fonksiyonlarında bulunur ve ekrana yazdırılır.'''
for number in range(0,1001):
	if 0<=number<=500:
		prime_first(number)
	else:
		prime_second(number)


