import random, math

def tradicni_postup():
    guess = 50
    cislo = random.randint(1, 100)
    iteration = 0
    interval = [0, 100]

    while guess != cislo:
        if guess > cislo:
            interval = [interval[0], guess]
        elif guess < cislo:
            interval = [guess, interval[1]]
        
        prev_guess = guess
        guess = math.floor(interval[0] + ((interval[1] - interval[0])/2))
        iteration += 1
        # print(f"Guess: {guess} interval: {interval}")
        if iteration > 50:
            print(f"Cislo je {cislo} a pocet iteraci byl {iteration}")
            raise RuntimeError("prdele")
        
        if guess == prev_guess:
            guess += 1

        if guess == cislo:
            break

    return iteration        
    # print(f"Cislo je {cislo} a pocet iteraci byl {iteration}")

def neo_postup():
    guess = random.randint(1, 100)
    cislo = random.randint(1, 100)
    iteration = 0
    interval = [0, 100]

    while guess != cislo:
        if guess > cislo:
            interval = [interval[0], guess]
        elif guess < cislo:
            interval = [guess, interval[1]]
        
        guess = random.randint(interval[0], interval[1])
        iteration += 1
        # print(f"Guess: {guess} interval: {interval}")
        if iteration > 50:
            raise RuntimeError
        if guess == cislo:
            break
    return iteration

    # print(f"Cislo je {cislo} a pocet iteraci byl {iteration}")

n_iter = int(input("Pocet iteraci: "))



tradicni = [tradicni_postup() for i in range(0,n_iter)]
neo = [neo_postup() for i in range(0,n_iter)]
# print(str(tradicni) + "\n \n" + str(neo))

tradicni_prumer = sum(tradicni)/len(tradicni)
neo_prumer = sum(neo)/len(neo)
print(f"Prumer tradicniho postupu je {tradicni_prumer} a neo postupu je {neo_prumer}")