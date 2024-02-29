a = int(input("Přirozené číslo: "))
pocet_delitelu = 0

for delitel in range(2, a+1):
    if a % delitel == 0:
        pocet_delitelu += 1

if pocet_delitelu == 1 and a != 1:
    print(f"Zadané číslo {a}, je prvočíslo")
else:
    print(f"Zadané číslo {a}, není prvočíslo")
