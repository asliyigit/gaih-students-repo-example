#Kod açıklanmıştır

'''
SORU:
Tarif Uygulaması
3 tarif girin. Her tarif için ayrı bir sınıf oluşturun.
init() metodunu kullanarak bu tarifte kullanılan ürünleri tanımlayın.
Bu ürünlerin daha sonra ne kadar süre kullanılması gerektiğiyle ilgili bir fonksiyon yazın.

Burada mirası kullanmayı unutmayın. Burada kalıtım kullanmak için;
Örneğin;
Yemek pişirme fonksiyonunu yazın. Bu yöntem tüm sınıflar için ortak olacağından, burada kalıtımı kullanmanız gerekir.'''


'''
KODLARDA
---------
YemekTarifi Sınıfında aşağıdaki metotlar bulunmaktadır:
constructor()
malzemeler()
hazirlanisi()
icHarciHazirlama()
serbetHazirlama()
tuzEkleme()
karabiberEkleme()
pisirme()
pufNoktalar()

Mucver Sınıfında aşağıdaki metotlar YemekTarifi sınıfından miras alınarak uygulanmıştır.
constructor()
malzemeler()
tuzEkleme()
karabiberEkleme()
hazirlanisi()
pisirme()
pufNoktalar()

Sarma Sınıfında aşağıdaki metotlar YemekTarifi sınıfından miras alınarak uygulanmıştır.
constructor()
malzemeler()
icHarciHazirlama()
tuzEkleme()
karabiberEkleme()
hazirlanisi()
pisirme()
pufNoktalar()

Revani Sınıfında aşağıdaki metotlar YemekTarifi sınıfından miras alınarak uygulanmıştır.
constructor
malzemeler()
serbetHazirlama()
hazirlanisi()
pisirme()
pufNoktalar()
'''

#Programda SuperClass olarak kullanılacak olan YemekTarifi sınıfı
class YemekTarifi(): 
    def __init__(self,yemekAdi): #constructor(yapıcı)->class nesne ile çağırıldıgında ilk olarak yapıcı çalışır
        self.yemekAdi=yemekAdi

    def malzemeler(self,malzeme):#yemeklerin malzemeleri bu metottan kalıtım yolu ile çağırılacaktır
        self.malzeme=malzeme
        print("\nMALZEMELER:")

    def hazirlanisi(self,hazirlanis):#yemeklerin hazırlama yöntemleri hazirlanisi() metodu ile kalıtım yoluyla çağırılacaktır
        self.hazirlanis=hazirlanis
        print("\nHAZIRLANIŞI:")

    def icHarciHazirlama(self,harc):#Sarma sınıfında iç harcı hazılamak için kullanılacak
        self.harc=harc
        print("\nİÇ HARCI HAZIRLAMA:")

    def serbetHazirlama(self,serbet):
        self.serbet=serbet
        print("\nŞERBET HAZIRLAMA:")

    def tuzEkleme(self,tuzEkle): #tuz eklenecek Sarma ve Mucver yemeklerinde tuzEkleme() metodu kullanılacaktır
        self.tuzEkle=tuzEkle
        print("\nEKLENECEK TUZ MİKTARI:")

    def karabiberEkleme(self,karabiberEkle):#karabiber eklenecek Sarma ve Mucver yemeklerinde karabiberEkleme() metodu kullanılacaktır
        self.karabiberEkle=karabiberEkle
        print("\nEKLENECEK KARABİBER MİKTARI:")

    def pisirme(self,pisir):#yemeklerin pişirilmesi gereken süre pisirme() metodu ile miras bırakılacaktır
        self.pisir=pisir
        print("\nPİŞİRMESİ")

    def pufNoktalar(self,pufNokta):#yemeklerin püf noktaları gereken süre pufNoktalar() metodu ile miras bırakılacaktır
        self.pufNokta=pufNokta
        print("\nPÜF NOKTALARI:")

#YemekTarifi sınıfından kalıtım ile miras alınan Mucver sınıfı(SubClass)
class Mucver(YemekTarifi):
    def __init__(self,yemekAdi):#constructor(yapıcı)->class nesne ile çağırıldıgında ilk olarak yapıcı çalışır
        yemekAdi="Mucver"
        super().__init__(yemekAdi)
        print("Mucver Sınıfı:")
    
    def malzemeler(self):
        malzeme="3 adet kabak\n2 adet yumurta(çırpılmış)\n1 adet havuç\n3 kahve fincanı un\n1 demet taze soğan\n1 demet dere otu"
        super().malzemeler(malzeme)
        print(f"{self.malzeme}")
        

    def hazirlanisi(self):
        hazirlanis="1.Bol suda yıkadığınız kabakları rendenin iri kısmıyla rendeleyin.\n2.Mücveri sulandırmaması için; rendelenmiş kabakların suyunu sıkarak çıkartın.\n3.Geniş bir kapta rendelenen kabakları, havucu, 2 adet çırpılmış yumurtayı, 1 demet taze soğanı, 1 demet dereotunu, 1 tatlı kaşığı tuzu, karabiberi ve 3 kahve fincanı unu birleştirin.\n4.Tüm malzemeler birbiriyle harmanlanıp, macun kıvamını alana kadar spatula yardımıyla karıştırın.\n5.Her bir mücver 1 tepeleme yemek kaşığı olacak şekilde ayarlayın."
        super().hazirlanisi(hazirlanis)
        print(f"{self.hazirlanis}")

    def tuzEkleme(self):
        tuzEkle="1 çay kaşığı tuz ekle"
        super().tuzEkleme(tuzEkle)
        print(f"{self.tuzEkle}")

    def karabiberEkleme(self):
        karabiberEkle="1 çay kaşığı karabiber ekle"
        super().karabiberEkleme(karabiberEkle)
        print(f"{self.karabiberEkle}")

    def pisirme(self):
        pisir="1.Kızgın yağda altın sarısı rengini alana kadar kızartın.\n2.Mücverlerin fazla yağını havlu kağıda süzdürdükten sonra servis tabağına alın ve çırpılmış yoğurt ile servis edin."
        super().pisirme(pisir)
        print(f"{self.pisir}")

    def pufNoktalar(self):
        pufNokta="İyi pişirin"
        super().pufNoktalar(pufNokta)
        print(f"{self.pufNokta}")


#YemekTarifi sınıfından kalıtım ile miras alınan Sarma sınıfı(SubClass)
class Sarma(YemekTarifi):
    def __init__(self,yemekAdi):#constructor(yapıcı)->class nesne ile çağırıldıgında ilk olarak yapıcı çalışır
        yemekAdi="Sarma"
        super().__init__(yemekAdi)
        print("\nSarma Sınıfı:")
    
    def malzemeler(self):
        malzeme="300 gram asma yaprağı\n1 adet limon\n4 yemek kaşığı zeytinyağı\n1 su bardağı sıcak su"
        super().malzemeler(malzeme)
        print(f"{self.malzeme}")
        
    def icHarciHazirlama(self):
        harc="1/2 su bardağı zeytinyağı\n3 adet orta boy kuru soğan\n1,5 su bardağı pirinç\n1 su bardağı sıcak su\n1 yemek kaşığı dolmalık fıstık\n1 yemek kaşığı kuş üzümü"
        super().icHarciHazirlama(harc)
        print(f"{self.harc}")

    def hazirlanisi(self):
        hazirlanis="1.Sarmanın iç harcını hazırlamak için; yarım su bardağı zeytinyağını geniş tabanlı bir tencerede kızdırın. 3 adet rendelenmiş soğanı hafif renk alana kadar kavurun. Ardından üzerine 1,5 yemek kaşığı dolmalık fıstığı da  koyup kavurmaya devam edin.\n2.Salamura asma yapraklarını tezgahın üzerinde damarlı kısımları üstte kalacak şekilde açın. Her bir yaprağın orta kısmına; hazırlayıp, ılıttığınız iç harçtan birer tatlı kaşığı kadar paylaştırın\n3.Kenar kısımlarını içe alıp, geniş kısmından uç kısmına doğru ilerleyin."
        super().hazirlanisi(hazirlanis)
        print(f"{self.hazirlanis}")

    def tuzEkleme(self):
        tuzEkle="1 çay kaşığı tuz ekle"
        super().tuzEkleme(tuzEkle)
        print(f"{self.tuzEkle}")

    def karabiberEkleme(self):
        karabiberEkle="1 çay kaşığı karabiber ekle"
        super().karabiberEkleme(karabiberEkle)
        print(f"{self.karabiberEkle}")

    def pisirme(self):
        pisir="Yemeği pişirirken üzerine porselen tabak kapatarak buharlı bir şekilde düzgünce pişmesine yardımcı olursunuz"
        super().pisirme(pisir)
        print(f"{self.pisir}")

    def pufNoktalar(self):
        pufNokta="Mümkünse; mevsiminde, az damarlı, taze asma yaprağı kullanın.Salamura yaprak kullanıyorsanız; tuzunun gitmesi için bol suda yıkayın. Kaynar suda 2- 3 dakika haşladıktan sonra durulayıp kullanın.Sarmaları sararken olabildiğince küçük ve sıkı sarılmasına özen gösterin.Kuş üzümlerini kumunun gitmesi için; bol suda bekletip, duruladıktan sonra kullanın."
        super().pufNoktalar(pufNokta)
        print(f"{self.pufNokta}")


#YemekTarifi sınıfından kalıtım ile miras alınan Revani sınıfı(SubClass)
class Revani(YemekTarifi):
    def __init__(self,yemekAdi):#constructor(yapıcı)->class nesne ile çağırıldıgında ilk olarak yapıcı çalışır
        yemekAdi="Revani"
        super().__init__(yemekAdi)
        print("\nRevani Sınıfı:")
    
    def malzemeler(self):
        malzeme="3 yumurta\n1 su bardağı şeker\n1 su bardağı yoğurt\n1 su bardağı irmik\n1 su bardağı un\n1 paket vanilya\n1 paket kabartma tozu\n1 çay bardağı sıvı yağ"
        super().malzemeler(malzeme)
        print(f"{self.malzeme}")
        
    def serbetHazirlama(self):
        serbet="3 su bardağı su\n3 su bardağı seker\n1/2 limon suyu"
        super().serbetHazirlama(serbet)
        print(f"{self.serbet}")

    def hazirlanisi(self):
        hazirlanis="1.İlk olarak şerbet hazırlanır. Şerbet için tencereye şeker ve su alınarak kaynatılır. Kaynadıktan sonra yarım limon suyu eklenip 1-2 dakika daha kaynatılıp altı kapatılır.\n2.Kek için, yumurta ve şeker çırpma kabına alınarak iyice çırpılır.\n3.Ardından sıvı yağ, yoğurt ve irmik eklenip çırpılır.\n4.Son olarak un, kabartma tozu ve vanilya da eklenerek iyice çırpılır.\n5.Yağlamış olduğumuz fırın kabına kek hamuru dökülür."
        super().hazirlanisi(hazirlanis)
        print(f"{self.hazirlanis}")

    def pisirme(self):
        pisir="170 derece fırında üstü kızarana dek yaklaşık 30 dakika pişirilir"
        super().pisirme(pisir)
        print(f"{self.pisir}")

    def pufNoktalar(self):
        pufNokta="*Şerbetinizin soğuması için keki yapamaya başlamadan önce yapılmalıdır.\n*Kekinizin kabarması için tüm malzemeleri oda sıcaklığında bulundurmalısınız.\n*Yumurta ile şeker köpük köpük oluncaya kadar çırpılmalıdır.\n*Şerbeti döktüğünüzde kek sıcak şerbet ise soğuk olmalıdır."
        super().pufNoktalar(pufNokta)
        print(f"{self.pufNokta}")

      
yemek = YemekTarifi("Mucver")
#yemek.hazirlanisi()

yemek1 = Mucver("Mucver")
yemek1.malzemeler()
yemek1.tuzEkleme()
yemek1.karabiberEkleme()
yemek1.hazirlanisi()
yemek1.pisirme()
yemek1.pufNoktalar()

yemek2 = Sarma("Sarma")
yemek2.malzemeler()
yemek2.icHarciHazirlama()
yemek2.tuzEkleme()
yemek2.karabiberEkleme()
yemek2.hazirlanisi()
yemek2.pisirme()
yemek2.pufNoktalar()

yemek3=Revani("Revani")
yemek3.malzemeler()
yemek3.serbetHazirlama()
yemek3.hazirlanisi()
yemek3.pisirme()
yemek3.pufNoktalar()
