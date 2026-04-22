from moduller.hesap_makinesi import hesap_makinesi
        
def ana_menu():
    print("\nPYTHON PROJE")
    print("1- Hesap Makinesi")
    print("0- Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        hesap_makinesi()
    elif secim == "0":
        return
    ana_menu()

ana_menu()