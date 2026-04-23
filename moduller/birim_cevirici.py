
def birim_cevirici():
    print("\nBİRİM ÇEVİRİCİ")
    print("1- kgf -> Newton")
    print("2- MPa -> kN/m²")
    print("3- m³ -> litre")
    print("4- kN -> ton")
    print("0- Ana Menü")

    secim = input("Seçiminiz: ")

    if secim == "1":
        kgf = float(input("kgf değeri: "))
        newton = kgf * 9.81
        print("Sonuç:", newton, "N")
        birim_cevirici()
        
    elif secim == "2":
        MPa = float(input("MPa değeri: "))
        kN_m2 = MPa * 1000
        print("Sonuç:", kN_m2, "kN/m²")
        birim_cevirici()
    
    elif secim == "3":
        m3 = float(input("m3 değeri: "))
        litre = m3 * 1000
        print("Sonuç: ", litre, "litre")
        birim_cevirici()
    
    elif secim == "4":
        kN = float(input("kN değeri: "))
        ton = kN / 9.80665
        print(f"Sonuç: {ton:.2f} ton")
        birim_cevirici()
    
    elif secim == "0":
        print("Ana menüye dönülüyor")
        return
    
    else:
        print("Hatalı seçim")
        birim_cevirici()
        
        