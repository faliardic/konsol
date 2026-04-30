from moduller.hesap_makinesi import hesap_makinesi
from moduller.bmi import bmi_hesapla
from moduller.birim_cevirici import birim_cevirici
from moduller.matoyun_1 import carpma_oyun
from moduller.sifre import sifre
from moduller.yakıt import yakit

        
def ana_menu():
    print("\nPYTHON PROJE")
    print("1- Hesap Makinesi")
    print("2- Vücut Kitle İndeksi")
    print("3- Birim çevirici")
    print("4- Çarpma Oyunu")
    print("5- Şifre Üretici")
    print("6- Araç Yakıt Hesabı")
    print("0- Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        hesap_makinesi()
    if secim == "2":
        bmi_hesapla()
    if secim == "3":
        birim_cevirici()
    if secim == "4":
        carpma_oyun()
    if secim == "5":
        sifre()
    if secim == "6":
        yakit()
    elif secim == "0":
        return
    ana_menu()

ana_menu()