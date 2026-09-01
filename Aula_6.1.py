import math

caso = 1

while True:
    N = int(input())

    if N == 0:
        break

    consumo = {}

    totalpessoas = 0
    totalconsumo = 0

    for _ in range(N):
        pessoas, quantidade = map(int, input().split())

        totalpessoas += pessoas
        totalconsumo += pessoas * quantidade

        consumo[quantidade] = consumo.get(quantidade, 0) + pessoas

    valores = sorted(consumo.items())

    print(f"Cidade# {caso}:")

    resultado = []

    for quantidade, pessoas in valores:
        resultado.append(f"{pessoas}-{quantidade}")
    print(" ".join(resultado))

    media = totalconsumo / totalpessoas

    media = math.floor(media * 100) / 100

    print(f"Consumo medio: {media:.2f} m3")
    print()

    caso += 1

    
