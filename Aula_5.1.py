n = int(input())

for caso in range(n):
    texto = input()

    frequencia = {}

    for caractere in texto:
        codigo = ord(caractere)

        if codigo not in frequencia:
            frequencia[codigo] = 0

        frequencia[codigo] +=1
    caractere = list(frequencia.keys())
    caractere.sort(
        key = lambda codigo: (frequencia[codigo], -codigo)
    )
    for codigo in caractere:
        print(codigo,frequencia[codigo])

    if caso < n - 1:
        print()