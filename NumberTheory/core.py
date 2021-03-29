import math


__all__ = ['sito', 'fact', 'tot', 'primes', 'nwd']


def sito(u):
    tab = [0 for i in range(u+1)]
    for i in range(2, u+1):
        tab[i] = i
    for i in range(4, u+1, 2):
        tab[i] = 2
    for i in range(3, math.floor(math.sqrt(u))):
        if tab[i] == i:
            for j in range(i*i, u+1, i):
                if (tab[j] == j):
                    tab[j] = i
    return tab


def fact(x, licz):
    primes = []
    counts = []
    primes.append(licz[x])
    counts.append(1)
    x = x // licz[x]
    while x > 1:
        if licz[x] == primes[-1]:
            counts[-1] += 1
            x = x // licz[x]
        else:
            primes.append(licz[x])
            counts.append(1)
            x = x // licz[x]
    wyn = [primes, counts]
    return wyn


def primes(x, licz):
    primes = []
    while x > 1:
        if licz[x] in primes:
            x = x // licz[x]
        else:
            primes.append(licz[x])
            x = x // licz[x]
    return primes


def tot(x, licz):
    p = primes(x, licz)
    if x == 0:
        return 0
    else:
        wyn = x
        for i in p:
            wyn *= (1-1/i)
        return int(wyn)


def nwd(a, b):
    while b > 0:
        c = a % b
        a = b
        b = c
    return a
