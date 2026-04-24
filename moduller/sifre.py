import random

def sifre():
    print("Şifre Üretici")
    print("1- 4 hane pin")
    print("2- 6 hane pin")
    print("3- 6 hane şifre")
    print("4- 8 hane şifre")
    print("0- Ana menü")
    
    secim = input("Seçiminiz: ")
    
    if secim == "1":
        dortPin = random.randint(1000, 9999)
        print(dortPin)
        sifre()
    
    if secim == "2":
        altiPin = random.randint(100000, 999999)
        print(altiPin)
        sifre()
    
    if secim == "3":
        karakterler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"

        sifre = ""
        for i in range(6):
            sifre += random.choice(karakterler)

        print("Şifre:", sifre)
                       
    if secim == "4":
        karakterler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"

        sifre = ""
        for i in range(8):
            sifre += random.choice(karakterler)

        print("Şifre:", sifre)
            
    if secim == "0":
        return
        
