def ordenacao(pre, posicoes, inicio, fim, resultado, indice):
    if inicio > fim:
        return
    raiz = pre[indice[0]]
    indice[0] += 1
    folhas = posicoes[raiz]
    ordenacao(pre, posicoes, inicio, folhas - 1, resultado, indice)
    ordenacao(pre, posicoes, folhas + 1, fim, resultado, indice)

    resultado.append(raiz)
casos = int(input())
for repeticao in range(casos):
    N, prefixa, infixa = input().split()
    N = int(N)

    posicoes = {}

    for i in range(N):
        posicoes[infixa[i]] = i
    resultado = []
    ordenacao(prefixa, posicoes, 0, N - 1, resultado, [0])
    print("".join(resultado))