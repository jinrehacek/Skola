def fibonacci_seq(n_clen):
    iter = 1
    prvni = 0
    dalsi = 1
    pamet = 0

    if n_clen == 0:
        return 0
    
    while n_clen > (iter):
        pamet = dalsi
        dalsi = prvni + dalsi
        prvni = pamet
        iter += 1

    return dalsi

n_clenu = int(input("Jaký člen z fib.: "))

print(fibonacci_seq(n_clenu))