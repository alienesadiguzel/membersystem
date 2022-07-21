import random

class uyelikSistemi:
    def __init__(self,kullaniciAdi=[],sifre=[]):
        self.kullaniciAdi=kullaniciAdi
        self.sifre=sifre
        self.siteDurum=True
        self.siteIsim="Ali'nin İşhanı"
        self.hesapDurumu=True
        
    def menuSecimEkrani (self):
        print("""\n---------------{} hoşgeldiniz!!!--------------- \n 
                           1- Giriş Yap \n 
                           2- Üye Ol \n 
                           3- Şifremi Unuttum \n""".format(self.siteIsim))
         
    def secim(self):
        sec=int(input("Lütfen yapmak istediğiniz işlemi giriniz: "))
        return sec
    
    def islem(self):
        self.menuSecimEkrani()
        
        Secim=self.secim()
        sayac=0
        if Secim==1:
            while self.hesapDurumu:
                kA=(input("Lütfen Kullanıcı Adınızı Giriniz: "))
                if kA in self.kullaniciAdi:
                    Sifre=(input("lütfen Şifrenizi Giriniz: "))  
                    if Sifre in self.sifre:
                        print("Tebrikler Başarıyla Giriş Yaptınız!!")
                    else:
                        print("Şifreniz Yanlıştır Lütfen Tekrar Deneyiniz.")
                        sayac+=1
                        if sayac == 2:
                            self.hesapDurumu=False
                            print("hesabınız askıya alındı!")
                            self.siteDurum=False
                            
                else:
                    print("böyle bir hesap bulunamadı!")
                
        if Secim==2:
            kayitAdi= input("Lütfen Kayıt Olmak İçin Kullanıcı Adı Giriniz: ")
            self.kullaniciAdi.append(kayitAdi)
            kayitSifre= input("Lütfen Kayıt Olmak İçin Şifre Giriniz: ")
            self.sifre.append(kayitSifre)
        
        if Secim==3:
           kontrol=input("Lütfen Kullanıcı Adınızı Giriniz: ")
           if kontrol in self.kullaniciAdi:
               Random=random.randint(1,100)
               print(Random)
               rastgeleSayi=int(input("Lütfen size gelen sayiyi buraya giriniz: "))
               if Random==rastgeleSayi:
                   yeniSifre=input("Lütfen Yeni Şifrenizi Giriniz: ")
                   self.sifre.append(yeniSifre)
                   
               else:
                   print("Sayılar Aynı Değil!!")
           else:
              print("böyle bir kullanıcı adi bulunamadı!!")
           
            
uye=uyelikSistemi()

while uye.siteDurum:
        uye.islem()
        