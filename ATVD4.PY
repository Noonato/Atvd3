from math import sqrt
from time import time

def Dados(n):
    return int(n) == n

def NumeroPrimo(n, showStatusFlag=False):
    if n == 2:
        return True
    elif (n == 1) or (n % 2 == 0) or (Dados(sqrt(n))):
        return False
    else:
        primoFlag = True
        limite = int(sqrt(n))

        if limite % 2 == 0:
            d = limite + 1
        else:
            d = limite
        o = n / d
        if (o <= d):
            return primoFlag

        d = 1
        div = 0
        count = 0
        while (d <= limite) and (div <= 2):
            count = count + 1
            if (n % d == 0):
                div = div + 1
                if (div == 2) and (d != n):
                    primoFlag = False
                    break
            d = d + 2

        if showStatusFlag:
            print('n:', n, 'd:', d, 'count:', count, 'div:', div)

        return primoFlag

def Primos2(n, showStatusFlag=False):
    if n == 2:
        return True
    elif (n == 1) or (n % 2 == 0) or (Dados(sqrt(n))):
        return False
    else:
        primoFlag = True
        limite = int(sqrt(n))

        if limite % 2 == 0:
            d = limite + 1
        else:
            d = limite
        o = n / d
        if (o <= d):
            return primoFlag

        d, o, r = 1, 0, 0

        div = 0
        count = 0
        while (d <= limite) and (div <= 2):
            count = count + 1

            r = n % d

            if (r == 0):
                div = div + 1
                if (div == 2) and (d != n):
                    primoFlag = False
                    break
            else:
                o = n / d
                if (o <= d):
                    primoFlag = True
                    break
            d = d + 2
        if showStatusFlag:
            print('n:', n, 'd:', d, 'o:', o, 'r:', r, 'count:', count, 'div:', div)
        return primoFlag

def primos(max):
    primosArr = []
    for i in range(1, max + 1):
        if NumeroPrimo(i):
            primosArr.append(i)
            print(i, "Verdadeiro")
        else:
            print(i, "Falso")
    return primosArr

gg = time()
print(primos(100))


