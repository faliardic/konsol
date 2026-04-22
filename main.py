def hesap_makinesi():
    print("\nHESAP MAKİNESİ")
    print("1- Toplama")
    print("2- Çıkarma")
    print("0- Ana Menü")

    secim = input("Seçiminiz: ")

    if secim == "1":
        toplama()
        hesap_makinesi()
    elif secim == "2":
        cikarma()
        hesap_makinesi()
    elif secim == "0":
        return
    
def toplama():
    a = float(input("1. sayı: "))
    b = float(input("2. sayı: "))
    print("Sonuç:", a + b)
    
def cikarma():
    a = float(input("1. sayı: "))
    b = float(input("2. sayı: "))
    print("Sonuç:", a - b)
        
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