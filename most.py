import random

POCET_POKUSU = 500000
SIRKA_MOSTU = 20
DELKA_MOSTU = 50

class Namornik:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.alive = True

def prejiti_mostu() -> bool:
    namornik = Namornik(random.randint(0, (SIRKA_MOSTU-1)), 0)

    while namornik.alive == True:
        namornik.y += 1
        namornik.x = namornik.x + random.choice([-1, 1])
        
        # print(str(namornik.x) + " " + str(namornik.y))

        if namornik.x < 0 or namornik.x > (SIRKA_MOSTU-1):
            namornik.alive = False
            # print("Namornik umrel")
            return False
        if namornik.y == (DELKA_MOSTU):
            # print("Namornik prezil")
            return True

prezivani = 0
umrtnost = 0

for i in range(0, POCET_POKUSU):
    if prejiti_mostu() == True:
        prezivani += 1
    if prejiti_mostu() == False:
        umrtnost = umrtnost + 1

statistika = prezivani/POCET_POKUSU

print(prezivani)
print(statistika)



