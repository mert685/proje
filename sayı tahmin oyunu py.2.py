# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 22:54:03 2026

@author: PC
"""

import random 


 
def sayi_tahmin_oyunu():
    hedef_sayi = random.randint(1, 100) 
    tahmin_hakki = 7
    
    print("--- SAYI TAHMİN OYUNU ---")
    print("1 ile 100 arasında bir sayı tuttum. 7 hakkın var!\n")

    for hak in range(1, tahmin_hakki + 1):
        try:
            tahmin = int(input(f"{hak}. Tahmininiz: "))
        except ValueError:
            print("Lütfen geçerli bir sayı girin!")
            continue 
        
        if tahmin == hedef_sayi:
            print(f"Tebrikler! {hak}. denemede doğru bildiniz!")
            break
        elif tahmin < hedef_sayi:
            print("Daha BÜYÜK bir sayı söyleyin.")
        else:
            print("Daha KÜÇÜK bir sayı söyleyin.") 
    else:
        print(f"\nHakkınız bitti! Tuttuğum sayı: {hedef_sayi}")



sayi_tahmin_oyunu 

























