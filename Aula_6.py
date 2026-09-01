from math import gcd

N = int(input())

for _ in range(N):

    n1, _, d1, operador, n2, _, d2 = input().split()

    n1 = int(n1)
    d1 = int(d1)
    n2 = int(n2)
    d2 = int(d2)

    if operador == "+":
        numerador = n1 * d2 + n2 * d1
        denominador = d1 * d2
    elif operador == "-":
            numerador = n1 * d2 - n2 * d1
            denominador = d1 * d2
    elif operador == "*":
            numerador = n1 * n2 
            denominador = d1 * d2
    else:
        numerador = n1 * d2 
        denominador = d1 * n2

    originalnumerador = numerador
    originaldenominador = denominador

    divisor = gcd(
          abs(numerador),
          abs(denominador)
    )

    numerador //= divisor
    denominador //=divisor

    if denominador < 0:
          numerador *= -1
          denominador *= -1

    print(
          f"{originalnumerador}/{originaldenominador} = "
          f"{numerador}/{denominador}"
    )
        