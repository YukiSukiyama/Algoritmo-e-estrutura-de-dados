casos = int(input())

for _ in range(casos):
    N = int(input())

    vagoes = list(map(int, input().split()))    
    trocas = 0

    for i in range(1,N):
        J = i

        while J > 0 and vagoes[J] < vagoes[J-1]:
            vagoes[J], vagoes[J - 1] = vagoes[J-1],vagoes[J]

            trocas += 1

            J -= 1

    print(f'Optimal Train Swapping takes {trocas} swaps')
