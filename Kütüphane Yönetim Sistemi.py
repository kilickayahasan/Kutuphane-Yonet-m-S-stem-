def kitap_ekle(ad, konu, sayfa):

    kitap =f"{ad},{konu},{sayfa}\n"

    with open("Kitaplık.txt", "a", encoding="utf-8") as file:

        file.write(kitap)

def kitap_cıkar(ad):

    with open ("Kitaplık.txt" , "r" , encoding ="utf-8") as file :
        kitaplar = file.readlines ()
        yeni_liste = []

        for kitap in kitaplar :
            if not kitap.startswith(ad + ",") :    ##  Eğer kitabın adı "ad" ile başlamıyorsa
                yeni_liste.append(kitap)           ## Bu kitabı yeni listeye ekle

    with open ("Kitaplık.txt" , "w" , encoding ="utf-8") as file :

        for i in yeni_liste:

            file.writelines (i)

while True:
    print("""

    İşlem Seçiniz :

    1. Kitap Ekleme
    2. Kitap Çıkarma
    3. Sistemden Çıkış


    """)

    işlem = int(input("İşlem Seçiniz : "))

    if işlem == 1:

        ad = input("Kitap Adını Giriniz : ")
        konu = input("Kitabın Konusunu Giriniz : ")
        sayfa = input("Sayfa Sayısını Giriniz : ")

        kitap_ekle(ad, konu, sayfa)

        print("Kütüphaneye {} isimli kitap eklendi !!!".format(ad))

    elif işlem == 2:
        ad = input("Silmek İstediğiniz Kitabın adını giriniz : ")

        kitap_cıkar(ad)

        print("Kütüphaneden {} isimli kitap çıkarıldı !!!".format(ad))

    elif işlem == 3:

        print("İşlem Sonlandırılıyor...")
        break











