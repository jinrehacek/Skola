""" Question:
V sportce se losuje 6 čísel ze 49. Jaká je pravděpodobnost, že vyhrajeme
a) druhou cenu (tipneme 5 čísel správně)
b) třetí cenu (tipneme 4 čísla správně)
pokud jsme tipovali jednu šestici čísel?
"""
import random

N_POKUSU = 100000000

num_pool = [i for i in range(1, 50)]
druha_cena, treti_cena = 0, 0

for i in range(N_POKUSU):
    my_selection = set(random.sample(num_pool, 6))
    vyherni = set(random.sample(num_pool, 6))
    
    stejne = my_selection.intersection(vyherni)
    pocet_stejnych = len(list(stejne))

    if pocet_stejnych == 5:
        druha_cena += 1
    elif pocet_stejnych == 4:
        treti_cena += 1

print(f"Druha cena byla {druha_cena}, treti cena byla {treti_cena}.")
print(f"Pravdepodobnost druhe ceny byla {100*(druha_cena/N_POKUSU)} %, treti cena byla {100*(treti_cena/N_POKUSU)} %")
