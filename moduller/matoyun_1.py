import random

def carpma_oyun():
    print("\nÇARPMA OYUNU")
    print("1- Oyuna Başla")
    print("0- Ana Menü")

    secim = input("Seçiminiz: ")

    if secim == "0":
        return
    elif secim != "1":
        print("Hatalı seçim")
        carpma_oyun()
        return

    sayi1 = random.randint(10, 99)
    sayi2 = random.randint(10, 99)
    carpim = sayi1 * sayi2

    print(sayi1, "x", sayi2)

    cevap = int(input("Cevabınız: "))

    while cevap != carpim:
        print("Yanlış cevap, tekrar deneyin.")
        print("Ana menü için '0' ")
        cevap = int(input("Cevabınız:  "))
        if cevap == 0:
            break

    print("Tebrikler! Doğru cevap.")