from moduller.hesap_makinesi import hesap_makinesi
from moduller.bmi import bmi_hesapla
from moduller.birim_cevirici import birim_cevirici
        
def ana_menu():
    print("\nPYTHON PROJE")
    print("1- Hesap Makinesi")
    print("2- Vücut Kitle İndeksi")
    print("3- Birim çevirici")
    print("0- Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        hesap_makinesi()
    if secim == "2":
        bmi_hesapla()
    if secim == "3":
        birim_cevirici()
    elif secim == "0":
        return
    ana_menu()

ana_menu()