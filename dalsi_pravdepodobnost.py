""" QUESTION
V bedně je 49 výrobků, z nich je pouze 6 dobrých. Náhodně z nich vytáhneme 6 výrobků. Jaká je pravděpodobnost, že z vytažených výrobků jsou alespoň čtyři dobré?
"""
import random

N_POKUSU = 100000

n_celkem = 49
n_good = 6
uspech = 0

vyrobky = ["F" for i in range(n_celkem-n_good)]
vyrobky.extend(["G" for i in range(n_good)])

for i in range(N_POKUSU):
    vybrane = random.sample(vyrobky, 6)
    if vybrane.count("G") >= 4:
        uspech +=1

print(uspech/N_POKUSU)