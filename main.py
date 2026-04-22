def hesap_makinesi():
    print("\nHESAP MAKİNESİ")
    print("1- Toplama")
    print("2- Çıkarma")
    print("0- Ana Menü")

    secim = input("Seçiminiz: ")

    if secim == "1":
        print("Toplama seçildi")
    elif secim == "2":
        print("Çıkarma seçildi")
    elif secim == "0":
        return
    
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