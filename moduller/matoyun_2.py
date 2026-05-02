
# iki kişilik sayı tahmin oyunu 
# 0 - 1000 arası

import random

def tahmin():
    sayı = random.randint(1,1000)
    
    player1 = input("1.Oyuncu ismi: ")
    player2 = input("2.Oyuncu ismi: ")
    
    
    while sayı < 1000:
        player1_tahmin = int(input(f"{player1} tahmin et:\n"))
    
        if player1_tahmin > sayı:
            print("İN")
            player2_tahmin = int(input(f"{player2} tahmin et\n"))
        
            if player2_tahmin > sayı:
                print("İN")
                continue
                
            elif player2_tahmin < sayı:
                print("ÇIK")
                continue
            
            elif player2_tahmin == sayı:
                print("DOĞRU!")
                print(f"{player2} KAZANDI!")
                break            
            
        elif player1_tahmin < sayı:
            print("ÇIK")
            player2_tahmin = int(input(f"{player2} tahmin et\n"))
        
            if player2_tahmin > sayı:
                print("İN")
                continue
                
            elif player2_tahmin < sayı:
                print("ÇIK")
                continue
            
            elif player2_tahmin == sayı:
                print("DOĞRU!")
                print(f"{player2} KAZANDI!")
                break
        
        
        elif player1_tahmin == sayı:
            print("DOĞRU!")
            print(f"{player1} KAZANDI!")
            break
        
        

        
        