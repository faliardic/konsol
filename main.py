from moduller.hesap_makinesi import hesap_makinesi
from moduller.bmi import bmi_hesapla
        
def ana_menu():
    print("\nPYTHON PROJE")
    print("1- Hesap Makinesi")
    print("2- Vücut Kitle İndeksi")
    print("0- Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        hesap_makinesi()
    if secim == "2":
        bmi_hesapla()
    elif secim == "0":
        return
    ana_menu()

ana_menu()