
def yakit():
    print("1- 1 km'de kaç tl")
    print("2- Kat edilen mesafe ve alınan yakıta bağlı değerler")
    print("0- Ana menü")
    
    secim = input("Seçiminiz: ")
    
    if secim == "1":
        yuz = float(input("100 km'de harcanan(lt): "))
        fiyat = float(input("Güncel yakıt fiyatı(₺): "))
        kmTl = yuz * fiyat / 100 
        print(f"Aracınız km'de {kmTl:.2f} ₺ yakmış")
        
    elif secim == "2":
        mesafe = float(input("Kat edilen mesafe(km): "))
        alYakLt = float(input("Alınan yakıt(lt): "))
        alYakTl = float(input("Alınan yakıt(tl): "))
        birLt = 100 * alYakLt / mesafe
        birTl = alYakTl / mesafe
        print(f"\n100 Kilometrede {birLt:.2f} lt ve,")
        print(f"1 Kilometrede {birTl:.2f} ₺ harcadınız")
    
    elif secim == "0":
        return
    
    else:
        print("Hatalı seçim")
    
