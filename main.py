def hesap_makinesi():
    print("\nHESAP MAKİNESİ")
    print("1- Toplama")
    print("2- Çıkarma")
    print("0- Ana Menü")

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