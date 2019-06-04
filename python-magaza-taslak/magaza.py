from pathlib import Path
dosya_adi = "kullanicilar.txt"

kolonlar = ['Marka', 'Model', 'Fiyat TL']
bilgisayar_dizustu = [
    ['Casper', 'Casper Wave', '1500'],
    ['Monster', 'Tulpar', '1200'],
    ['Acer', 'Predator', '1600']
]
bilgisayar_masaustu = [
    ['HP', 'Pavilion 690-0010', '500'],
    ['Dell', 'Inspiron 5680', '900'],
    ['Acer', 'Aspire', '800']
]

camasir_makinesi = [
    ['Arçelik', '12143 CMK', '1200'],
    ['Bosch', 'WAT24480TR', '500']
]
bulasik_makinesi = [
    ['Vestel', 'BM-301W', '250'],
    ['Vestfrost', 'VF BM 2003', '300']
]
cay = [
    ['Lipton', 'Yellow Label 1000 gr', '10'],
    ['Çaykur', '1000 gram', '10']
]
su = [
    ['Erikli', '1.5 lt', '3'],
    ['Nestle', '5 lt', '6']
]
cep_telefonu = [
    ['Samsung', 'Galaxy Note 9', '4000'],
    ['Iphone', '6S', '3000']
]
televizyon = [
    ['Vestel', '43UD8360', '2500'],
    ['Awox', 'AWX-10943ST', '1350']
]


def giris(secim):
    error = False
    error2 = False
    error3 = False
    j = 0
    while True:
        if secim == 'a':
            j = 0
            if not error:
                print("Boşluksuz yazın. Boşluk koyarsanız silinecektir.")
                isim = input("İsim girin: ").replace(" ", "")
                if isim == "":
                    print("Lütfen ismi boş bırakmayın", end=" ")
                    continue
                soyad = input("Soyad girin: ").replace(" ", "")
                if soyad == "":
                    print("Lütfen soyadı boş bırakmayın", end=" ")
                    continue
            kullaniciadi = input("Kullanıcı adı girin: ").replace(" ", "")
            if kullaniciadi == "":
                print("Lütfen kullanıcı adını boş bırakmayın", end=" ")
                continue
            error = False
            with open(dosya_adi) as f:
                content = f.readlines()
            content = [x.strip() for x in content]
            for kullanici in content:
                elemanlar = kullanici.split()
                if kullaniciadi == elemanlar[2]:
                    print("Böyle bir kullanıcı var")
                    error = True
                    break
            if error:
                continue
            sifre = input("Şifre girin: ").replace(" ", "")
            if sifre == "":
                print("Lütfen şifreyi boş bırakmayın", end=" ")
                continue
            with open(dosya_adi, "a") as f:
                f.write(str(isim+" "+soyad+" "+kullaniciadi+" "+sifre+"\n"))
            secim = 'b'
            print("Kullanıcı kaydı gerçekleşti. Lütfen giriş yapın. ")
            continue
        elif secim == 'b':
            with open(dosya_adi) as f:
                content = f.readlines()
            content = [x.strip() for x in content]

            if content == []:
                print("Kayıtlı kullanıcı bulunmamaktadır. Lütfen kayıt yapın. ")
                secim = 'a'
                continue
            else:
                kullaniciadi = input("Kullanıcı adı girin: ").replace(" ", "")

                for i in range(0, len(content)):
                    elemanlar = content[i].split()
                    if kullaniciadi == elemanlar[2]:
                        sifre = input("Şifre girin: ").replace(" ", "")
                        k = 0
                        while elemanlar[3] != sifre and k < 2:
                            sifre = input(
                                "Şifre yanlış. Doğru şifreyi girin: ").replace(" ", "")
                            k += 1
                        if k == 2:
                            soyad = input(
                                "3 kere hatalı giriş yaptınız. Lütfen kayıtlı soyadınızı girin: ")
                            if soyad == elemanlar[1]:
                                elemanlar[3] = input(
                                    "Soyad doğru. Yeni şifrenizi girin: ")
                                content[i] = ' '.join(elemanlar)
                                f = open(dosya_adi, "w")
                                for eleman in content:
                                    f.write(eleman+"\n")
                                f.close()
                                print("Şifreniz yenilendi. Lütfen giriş yapın. ")
                                giris('b')
                            else:
                                print(
                                    "Çok fazla hatalı işlem yaptınız. Giriş yapmak için yeni hesap açın. ")
                                giris('a')
                            error2 = True
                            break

                        if elemanlar[3] == sifre:
                            # kategoriler
                            print("Hoş geldiniz. ")
                            kategoriler(input(
                                "Hangi kategoride dolaşmak istiyorsunuz?\n1. Bilgisayar\n2. Beyaz eşya\n3. Süpermarket\n4. Elektronik"))
                            error3 = True
                            break

                if error2 or error3:
                    break
                print("Böyle bir kullanıcı yok! ")
                j += 1
                if j == 3:
                    print(
                        "Çok fazla hatalı işlem yaptınız. Giriş yapmak için yeni hesap açın. ")
                    giris('a')
                    error2 = True
                    break

        else:
            secim = input("Lütfen a ya da b şıkkını seçin: ")


def ilksecim(secim):
    while True:
        if secim == '1':
            giris(
                input("a. Lütfen kayıt olun\nb. Kaydınız varsa lütfen giriş yapın.\n"))
            break
        elif secim == '2':
            # kategoriler
            print("Hoş geldiniz. ")
            kategoriler(input(
                "Hangi kategoride dolaşmak istiyorsunuz?\n1. Bilgisayar\n2. Beyaz eşya\n3. Süpermarket\n4. Elektronik"))
            break
        else:
            secim = input("Lütfen 1 ya da 2 şıkkını seçin: ")


def kolon():
    for kol in kolonlar:
        print(kol, end="\t")
    print()


def yazdirma(kol_isim):
    kolon()
    for kol in kol_isim:
        for ozellik in kol:
            print(ozellik, end="\t")
        print()


def altkolon(alt, isim1, isim2):
    while True:
        if alt == 'a':
            yazdirma(isim1)
            break
        elif alt == 'b':
            yazdirma(isim2)
            break
        else:
            alt = input("Lütfen a ya da b şıkkını seçin")


def kategoriler(secim):
    while True:
        if secim == '1':
            alt = input("a. Dizüstü Bilgisayar\nb. Masaüstü Bilgisayar\n")
            altkolon(alt, bilgisayar_dizustu, bilgisayar_masaustu)
            break
        elif secim == '2':
            alt = input("a. Çamasir Makinesi\nb. Bulaşık Makinesi\n")
            altkolon(alt, camasir_makinesi, bulasik_makinesi)
            break
        elif secim == '3':
            alt = input("a. Çay\nb. Su\n")
            altkolon(alt, cay, su)
            break
        elif secim == '4':
            alt = input("a. Cep Telefonu\nb. Televizyon\n")
            altkolon(alt, cep_telefonu, televizyon)
            break
        else:
            secim == input("Lütfen sıralanmış kategorilerden birini seçin. ")

    istek = input(
        "Daha gezinmek istiyor musunuz? Evet icin e, çıkış yapmak için başka bir tuşa basın. ")
    if istek == 'e':
        kategoriler(input(
            "Hangi kategoride dolaşmak istiyorsunuz?\n1. Bilgisayar\n2. Beyaz eşya\n3. Süpermarket\n4. Elektronik\n"))
    else:
        print("Yine Bekleriz! ")


# Programın başladığı yer
if not Path("./"+dosya_adi).is_file():
    f = open(dosya_adi, "a")
    f.close()

ilksecim(input("Merhaba. Ne yapmak istiyorsunuz?\n1. Alışveriş yapmak istiyorum\n2. Sadece gezinmek istiyorum.\n"))
