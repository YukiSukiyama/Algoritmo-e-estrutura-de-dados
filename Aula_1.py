from bisect import bisect_left

Caso = 1

while True:
    N, Q = map(int, input().split())

    if N == 0 and Q == 0:
        break
    marmores = []
    for _ in range(N):    
        marmores.append(int(input()))

    marmores.sort()

    print(f"CASE# {Caso}:")

    for _ in range(Q):
        numero = int(input())

        posicao = bisect_left(marmores, numero)

        if posicao < N and marmores[posicao]== numero:
            print(f"{numero} found at {posicao+1}")
        else:
            print(f"{numero} not found")
    Caso += 1