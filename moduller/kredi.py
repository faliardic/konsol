
def kredi():
    anaPara = float(input("Çekilmek istenen miktar(tl): "))
    faiz = float(input("Kredi faizi(%) ")) / 100
    vade = float(input("Vade(ay): "))
    
    if faiz == 0:
        taksit = int(anaPara / vade)
        geriOde = anaPara
        print("Aylık", taksit, "TL")
        print("Toplam ödeme", geriOde , "TL")
        return
    
    if vade == 0:
        print("Vade 0 olamaz")
        return
    
    taksit = int(anaPara * (( faiz * ( 1 + faiz )**vade ) / (( 1 + faiz)**vade - 1)))
    geriOde = int(taksit * vade)
    
    print("Aylık", taksit, "TL")
    print("Toplam ödeme", geriOde , "TL")
    
  
