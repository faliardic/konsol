def bmi_hesapla():
    kilo = float(input("Kilonuz (kg): "))
    boy = float(input("Boyunuz (metre): "))
    
    bmi = kilo / (boy ** 2)
    
    print(f"\nVücut Kitle İndeksi: {bmi:.2f}")
    
    if bmi < 18.5:
        print("Zayıf")
    elif bmi < 25:
        print("Normal")
    elif bmi < 30:
        print("Fazla kilolu")
    else: 
        print("Obez")
    