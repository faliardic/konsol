import math

def hesap_makinesi():
    print("\nHESAP MAKİNESİ")
    print("1- Toplama")
    print("2- Çıkarma")
    print("3- Çarpma")
    print("4- Bölme")
    print("5- Karekök")
    print("0- Ana Menü")

    secim = input("Seçiminiz: ")

    if secim == "1":
        toplama()
        hesap_makinesi()
    elif secim == "2":
        cikarma()
        hesap_makinesi()
    elif secim == "3":
        carpma()
        hesap_makinesi()
    elif secim == "4":
        bolme()
        hesap_makinesi()
    elif secim == "5":
        karekok()
        hesap_makinesi()   
    elif secim == "0":
        return
    else:
        print("Geçersiz seçim")
        hesap_makinesi()
    
def toplama():
    a = float(input("1. sayı: "))
    b = float(input("2. sayı: "))
    print("Sonuç:", a + b)
    
def cikarma():
    a = float(input("1. sayı: "))
    b = float(input("2. sayı: "))
    print("Sonuç:", a - b)
        
def carpma():
    a = float(input("1. sayı: "))
    b = float(input("2. sayı: "))
    print("Sonuç:", a * b)
            
def bolme():
    a = float(input("1. sayı: "))
    b = float(input("2. sayı: "))

    if b == 0:
        print("0'a bölünemez")
        return

    print("Sonuç:", a / b)

def karekok():
    sayi = float(input("Sayı: "))

    if sayi < 0:
        print("Negatif sayının karekökü alınamaz")
        return

    print("Sonuç:", math.sqrt(sayi))