casos = int(input())

for caso in range(casos):
    M, C = map(int, input().split())

    tabela = [[] for _ in range(M)]

    valores = list(map(int(input().split())))

    for valor in valores:
        posicao = valor % M

        tabela[posicao].append(valor)

    for i in range(M):
        print(f"{i} ->", end="")

        for valor in tabela[i]:
            print(f"{valor} ->", end="")

        print()

    if caso < casos - 1:
        print()
        