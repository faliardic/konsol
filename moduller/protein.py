import math

def protein_ihtiyaci():
    print("=== PROTEİN İHTİYACI HESAPLAMA ===")

    cins = input("Cinsiyetiniz (E/K): ").strip().lower()
    yas = float(input("Yaşınız: "))
    kilo = float(input("Kilonuz (kg): "))
    boy = float(input("Boyunuz (cm): "))

    aktif = input("""
Aktivite düzeyiniz:
1: Hareketsiz
2: Hafif aktif
3: Orta aktif
4: Çok aktif
5: Atlet düzeyi
Seçiminiz: """)

    hedef = input("""
Hedefiniz:
1: Sağlıklı yaşam
2: Hafif kas kazanımı
3: Kas kazanımı
4: Yağ kaybı + kas koruma
5: Sert definisyon
Seçiminiz: """)

    # Aktivite katsayısı
    if aktif == "1":
        a_kat = 1.2
    elif aktif == "2":
        a_kat = 1.375
    elif aktif == "3":
        a_kat = 1.55
    elif aktif == "4":
        a_kat = 1.725
    elif aktif == "5":
        a_kat = 1.9
    else:
        print("Hatalı aktivite seçimi.")
        return

    # BMR hesabı
    if cins == "e":
        bmr = 10 * kilo + 6.25 * boy - 5 * yas + 5
    elif cins == "k":
        bmr = 10 * kilo + 6.25 * boy - 5 * yas - 161
    else:
        print("Hatalı cinsiyet seçimi.")
        return

    tdee = bmr * a_kat

    # Yağ oranı tahmini
    print("\nYağ oranı tahmini için ölçü bilgileri alınacak.")
    bel = float(input("Bel çevresi (cm): "))
    boyun = float(input("Boyun çevresi (cm): "))

    bel_inch = bel / 2.54
    boyun_inch = boyun / 2.54
    boy_inch = boy / 2.54

    if cins == "e":
        yag_orani = 86.010 * math.log10(bel_inch - boyun_inch) - 70.041 * math.log10(boy_inch) + 36.76

    else:
        kalca = float(input("Kalça çevresi (cm): "))
        kalca_inch = kalca / 2.54

        yag_orani = (
            163.205 * math.log10(bel_inch + kalca_inch - boyun_inch)
            - 97.684 * math.log10(boy_inch)
            - 78.387
        )

    # Mantıksız sonuçları sınırlama
    if yag_orani < 5:
        yag_orani = 5
    elif yag_orani > 60:
        yag_orani = 60

    yag_kutlesi = kilo * yag_orani / 100
    yagsiz_kutle = kilo - yag_kutlesi

    # Efektif kilo hesabı
    if cins == "e":
        yuksek_yag = yag_orani > 25
    else:
        yuksek_yag = yag_orani > 35

    if yuksek_yag:
        efektif_kilo = yagsiz_kutle + 0.25 * yag_kutlesi
    else:
        efektif_kilo = kilo

    # Hedefe göre temel protein katsayısı
    if hedef == "1":
        k_base = 1.0
    elif hedef == "2":
        k_base = 1.4
    elif hedef == "3":
        k_base = 1.8
    elif hedef == "4":
        k_base = 2.0
    elif hedef == "5":
        k_base = 2.2
    else:
        print("Hatalı hedef seçimi.")
        return

    # Yaş düzeltmesi
    if yas < 30:
        k_age = 0
    elif yas < 45:
        k_age = 0.1
    elif yas < 60:
        k_age = 0.2
    else:
        k_age = 0.3

    # Aktiviteye bağlı antrenman düzeltmesi
    if aktif == "1":
        k_training = 0
    elif aktif == "2":
        k_training = 0.05
    elif aktif == "3":
        k_training = 0.1
    elif aktif == "4":
        k_training = 0.15
    else:
        k_training = 0.2

    # Hedef yağ kaybıysa ekstra koruma katsayısı
    if hedef == "4":
        k_deficit = 0.2
    elif hedef == "5":
        k_deficit = 0.3
    else:
        k_deficit = 0

    toplam_katsayi = k_base + k_age + k_training + k_deficit

    protein = efektif_kilo * toplam_katsayi

    alt_sinir = protein * 0.9
    ust_sinir = protein * 1.1

    print("\n=== SONUÇLAR ===")
    print(f"BMR: {bmr:.0f} kcal")
    print(f"TDEE: {tdee:.0f} kcal")
    print(f"Tahmini yağ oranı: %{yag_orani:.1f}")
    print(f"Yağsız vücut kütlesi: {yagsiz_kutle:.1f} kg")
    print(f"Efektif protein kilosu: {efektif_kilo:.1f} kg")
    print(f"Protein katsayısı: {toplam_katsayi:.2f} g/kg")
    print(f"Günlük protein hedefi: {protein:.0f} g")
    print(f"Önerilen aralık: {alt_sinir:.0f} - {ust_sinir:.0f} g/gün")


