import random

n_pokusu = int(input("Pocet iteraci: "))
vysledky = 0

for hozeni in range(n_pokusu):
    kostka = random.randint(1,6)
    if kostka == 1: vysledky += 1
    
statistika = vysledky/n_pokusu
print(f"Pravděpodobnost je: {statistika}")