#Kod açıklanmıştır

'''
SORU:
Adam asmaca oyunu (Hangman game)
Nesne Yönelimli programlama kullanarak klasik bir adam asmaca oyunu yazın.
OOP kullanmanız şartıyla dilediğiniz gibi yazabilirsiniz.
'''

import random as rnd

class HangMan(object):

	#asılacak olan gövdeler hang adında bir listede tutulur
    hang = []
    hang.append(' +---+')
    hang.append(' |   |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('     |')
    hang.append('=======')
    
	#oyuncunun gerçekleştirebileceği eylemler oyuncu adında listede tutulur
    oyuncu = {}
    oyuncu[0] = [' 0   |']
    oyuncu[1] = [' 0   |', ' |   |']
    oyuncu[2] = [' 0   |', '/|   |']
    oyuncu[3] = [' 0   |', '/|\\  |']
    oyuncu[4] = [' 0   |', '/|\\  |', '/    |']
    oyuncu[5] = [' 0   |', '/|\\  |', '/ \\  |']
    
	#oyunun ilerleyen zamanlarında oyuncunun eylemlerini gosteren liste
    goruntu = []
    
	#oyun içerisinde rastgele üretilecek kelimeler
    kelimeler = '''global ai turkish deep machine reinforcement learning'''.split()

    strBilgi='_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\'*-_-*\''


    def __init__(self, *args, **kwargs): #constructor
        i, j = 2, 0
        self.goruntu.append(self.hang[:])
        for k in self.oyuncu.values():
            goruntu2, j = self.hang[:], 0
            for m in k:
                goruntu2[i + j] = m
                j += 1
            self.goruntu.append(goruntu2)

    # kelimeSec(): rastgele kelime seçmek için kullanılan metottur. 
	# 0'dan self.kelimeler-1 'e kadar olan kelimeler stringinden rastgele bir tane kelime seçer ve seçilen kelime return edilir.
    def kelimeSec(self): 
        return self.kelimeler[rnd.randint(0, len(self.kelimeler) - 1)]
    
	# goruntuYazdir(): |', '/|\\  |', '/ \\  | bu işleçler ile şekillleri oluşturmak için kullanılan metottur.
    def goruntuYazdir(self, idx, kelimeUzunlugu):
        for i in self.goruntu[idx]: #çizgileri yazdırmak için kullanılan for dongusu
            print(i)
            
    #girisAl() metodu ile kullanıcıya sorular sorulur
    def girisAl(self, kelime, sonuc, eksikmi):
        tahmin = input()  # kullanıcıdan tahmin için giriş alınır

		# kullanıcı girişi boşluk, eksik, yok vs ise metot geriye False değerini döndürür 
        if tahmin == None or len(tahmin) != 1 or (tahmin in sonuc) or (tahmin in eksikmi): 
            return None, False
        sayac = 0
        dogrumu = tahmin in kelime  # kullanıcı tarafından girilen tahmin değeri kelime içerisindeki harflerden biri ise
        for i in kelime:  # kelimeye kadar bir sayac ile gezinti sağlanır
            if i == tahmin:  # eger i değeri girilen tahmine eşitse
				#score = 5
                sonuc[sayac] = i # sonucun sayacına kelimedeki i değerini atar
            sayac += 1 # ve sayacı bir artırır, kelime içerisinde gezinmek için
        return tahmin, dogrumu  # metot geriye tahmini veya kelime içerisinden doğru girilen sonucu döndürür

    def bilgi(self, bilgi):  # bilgi değerleri alınır
        lenn=len(self.strBilgi)
        print(self.strBilgi[:-3])
        print(bilgi)
        print(self.strBilgi[3:])
            
	# basla() metodu ile oyun başlar.		
    def basla(self):
        print('Adam asmaca oyununa hoş geldiniz !')
        kelime = list(self.kelimeSec()) #kelimeSec() metodu kelime seçilir ve seçilen kelime list fonksiyonu ile listeye dönüştürülür.
        sonuc = list('*' * len(kelime)) # kelimenin uzunlugu alınır ve uzunluk kadar * eklenir
        print('Kelime: ', sonuc)
        success, i, eksikmi = False, 0, []
        while i < len(self.goruntu)-1:
            print('Kelimeyi tahmin edin: ', end='')
            tahmin,dogrumu = self.girisAl(kelime, sonuc, eksikmi) # kullanıcıya sorular sormak için kullanılır
            if tahmin == None:
                print('Bu karakteri zaten girdiniz')
                continue # var olan karakter girişi yapıldıgı için döngünün başına dönülür
            print(''.join(sonuc))
            if sonuc == kelime: # sonuc kelimeye esit ise doğru sonuc bulunmustur
                self.bilgi('Tebrikler! Adam kurtuldu !')
                success = True
				#score = 10
                break
            if not dogrumu: 
                eksikmi.append(tahmin) # dogru sonuc degilse eksikmi listesine kullanıcı tahminleri eklenir. 
				#Bir daha aynı karakterleri girmemesi için.
				#score = -5
                i+=1
            self.goruntuYazdir(i, len(kelime))
            print('Eksik karakterler: ', eksikmi)
        
        if not success: #Sonuc basarılı degil ise 
			#score = -10
            self.bilgi('Kelime \''+''.join(kelime)+'\'. Adam Öldü !')

oyunaBasla = HangMan().basla()
