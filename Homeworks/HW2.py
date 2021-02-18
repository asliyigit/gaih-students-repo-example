#Kod açıklanmıştır

'''
HOMEWORK-2:
Bir okuldaki 5 öğrencinin notları hakkında bilgi içeren bir program yazın
Bu öğrencilerin notlarını bir listede tutun. (Ara sınav, final, ödev)
Öğrenci isimlerini bir listede tutun. (Ad Soyad)
Bir sözlükte öğrencilerin tüm bilgilerini içeren bir sözlük oluşturun.
Burada öğrencinin notlarını azalan sırayla sıralayın ve listeleyin ve en yüksek puanı alan öğrenciyi tebrik edin.'''

nameSurnameList=[]  #name ve surname değerlerini tutmak için oluşturulan liste
scoreList=[]  #midterm, final ve homework değerlerini tutmak için oluşturulan liste

for i in range(0,5): # for döngüsü ile 0-5'e kadar (5 dahil değil) gidilerek 5 öğrencinin bilgileri alınacaktır. 
	#name, surname, midterm,final ve homework değerleri kullanıcıdan alınır.
	name = str(input("name: ")) 
	surname = str(input("surname: "))
	midterm = float(input("midterm: "))
	final = float(input("final: "))
	homework = float(input("homework: "))

	#append metodu ile nameSurnameList ve scoreList listelerine kullanıcıdan alınan  
	#name, surname, midterm, final ve homework değerleri eklenir
	nameSurnameList.append(name+" "+surname) 
	scoreList.append(midterm)
	scoreList.append(final)
	scoreList.append(homework)
	

#information adında dictionary oluşturulur. Bu sözlük 5 öğrencinin name_surname, midterm, final ve homework
#değerlerini tutarak key ve valeus olarak saklar.
information={"name": [nameSurnameList[0],nameSurnameList[1],nameSurnameList[2],nameSurnameList[3],nameSurnameList[4]],
			"midterm":[scoreList[0],scoreList[3],scoreList[6],scoreList[9],scoreList[12]],
			"final":[scoreList[1],scoreList[4],scoreList[7],scoreList[10],scoreList[13]],
			"homework":[scoreList[2],scoreList[5],scoreList[8],scoreList[11],scoreList[14]]
}
print("\ninformation:")
print(information) #kontrol amaçlı information ekrana yazdırılır

average=[] #average listesi ile en başarılı öğrenciyi belirlemek için vize, final ve ödevlerin ortalamaları hesaplanacaktır 
for i in range(5): 
	average.append((information["midterm"][i]+information["final"][i]+information["homework"][i])/3)# information'da 
	#ilgili alanlardaki (midterm, final, homework) değerler (i'ler) alınır. Her öğrenci için (5 öğrenci) average hesaplanır.

print("\naverage:")
print(average) #kontrol amaçlı average listesi ekrana yazdırılır


'''En başarılı öğrencilerin notlarını azalan sırayla sıralama işlemi için Bubble Sort algoritması kullanıldı.
En yüksek ortalamayı bulurken temp değişkeninde average[j] değeri tutuldu, daha sonra average[i]'deki değer 
average[j]'ye atandı ve temp değişkeninde tutulan average[j] değeri average[i]'ye atandı.
Daha sonra information'da kullanıcıya ait bulunan bilgiler (name, midterm, final ve homework değerlerinin) yerlerini 
değiştirmek, sıralamak içinde aynı işlemler uygulandı.'''
for i in range(5):  
	for j in range(4):  
		if average[i] > average[j]:  
			temp = average[j]
			average[j] = average[i]
			average[i] = temp

			temp = information["name"][j]
			information["name"][j] = information["name"][i]
			information["name"][i] = temp

			temp = information["midterm"][j]
			information["midterm"][j] = information["midterm"][i]
			information["midterm"][i] = temp

			temp = information["final"][j]
			information["final"][j] = information["final"][i]
			information["final"][i] = temp

			temp = information["homework"][j]
			information["homework"][j] = information["homework"][i]
			information["homework"][i] = temp

#Bubble Sort algoritması ile sıralanan information yazdırıldı
print("\nSıralı information:\nname - midterm - final - homework - average") 
for i in range(5): 
	print(information["name"][i], information["midterm"][i], information["final"][i], information["homework"][i], average[i],sep="  ")

#En yüksek puanı alan öğrencye tebrik mesajı yazdırıldı
print("\nTebrikler ",information["name"][0], "En Yüksek Puanı Aldınız",sep=" ")
