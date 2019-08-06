import os
class Musteri():
    def __init__(self,ID,ISIM,PAROLA):
        self.ID = ID
        self.ISIM = ISIM
        self.PAROLA = PAROLA
        self.bakiye = 0
class Banka():
    def __init__(self):
        self.musteriler = list()

    def register(self,ID,ISIM,PAROLA):
        self.musteriler.append(Musteri(ID,ISIM,PAROLA))
        print("kayıt yapıldı.")

def main():
    banka = Banka()
    while True:
        os.system("cls")
        print("""
        [1] Banka müşterisiyim
        [2] Kayıt olmak istiyorum
        """)
        secim1 = int(input("İşlem seçiniz: "))
        if secim1 == 1:
            ids = list()
            for i in banka.musteriler:
                ids += i.ID
            ID = input("ID giriniz: ")
            if ID in ids:
                for musteri in banka.musteriler:
                    if ID == musteri.ID:
                        print("Hoşgeldiniz Sn:{}".format(musteri.ISIM))
                        parola = input("Parolanızı giriniz: ")
                        if parola == musteri.PAROLA:
                            print("Giriş başarılı!")
                            while True:
                                os.system("cls")
                                print("""
                                [1]Bakiye Görüntüle
                                [2]Para Yatır
                                [3]Para Çek
                                [4]Çıkış
                                """)
                                secim2= int(input("İşlem seçiniz: "))
                                if secim2 == 1:
                                    print("Bakiyeniz: {}".format(musteri.bakiye))
                                    input("İşlem yapmak için enter")
                                elif secim2 == 2:
                                    tutar = int(input("Yatırmak istediğiniz tutarı giriniz: "))
                                    secim3 =input("Hesabınıza {} TL yatırmak istediğinizden emin misiniz? E/H".format(tutar))
                                    if secim3 == "e" or secim3 == "E":
                                        musteri.bakiye += tutar
                                        print("Para yatırma işlemi başarılı")
                                    elif secim3 == "h" or secim3 == "H":
                                        print("İşleminiz iptal edildi")
                                    else:
                                        print("Hatalı giriş yaptınız")
                                elif secim2 == 3:
                                    tutar2 = int(input("Çekmek istediğiniz tutarı giriniz: "))
                                    secim3 = input(
                                        "Hesabınızdan {} TL çekmek istediğinizden emin misiniz? E/H".format(tutar2))
                                    if secim3 == "e" or secim3 == "E":
                                        musteri.bakiye -= tutar2
                                        print("Para çekme işlemi başarılı")
                                    elif secim3 == "h" or secim3 == "H":
                                        print("İşleminiz iptal edildi")
                                    else:
                                        print("Hatalı giriş yaptınız")
                                elif secim2 == 4:
                                    print("Hesaptan çıkış yapıldı")
                                    break
                                else:
                                    print("Hatalı giriş yaptınız.")
                        else:
                            print("Hatalı parola")
                    else:
                        print("Böyle bir kullanıcı yok")
            else:
                print("Böyle bir kullanıcı yok")
        elif secim1 == 2:
            id = input("ID: ")
            isim = input("İsim: ")
            parola = input("Parola: ")
            banka.register(id,isim,parola)
        else:
            print("Hatalı giriş")
main()