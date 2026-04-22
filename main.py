def ana_menu():
    print("\nPYTHON PROJE")
    print("1- Hesap Makinesi")
    print("0- Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        print("Hesap makinesi seçildi")
    elif secim == "0":
        return

ana_menu()