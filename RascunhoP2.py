fila = []
processamento = []
historico = []

while True:
    valor = input("Digite um código inteiro positivo (0 para encerrar): ")
    try:
        codigo = int(valor)
    except ValueError:
        print("Código inválido.")
        continue
    if codigo == 0:
        break
    if codigo < 0:
        print("Código negativo não permitido.")
        continue
    duplicado = False
    for v in fila:
        if v == codigo:
            duplicado = True
            print("Código duplicado. Não será armazenado.")
            break
    if not duplicado:
        fila.append(codigo)

if len(fila) == 0:
    print("Fila vazia!")
else:
    ordenada = fila[:]
    for i in range(len(ordenada)):
        for j in range(0, len(ordenada) - 1 - i):
            if ordenada[j] > ordenada[j + 1]:
                ordenada[j], ordenada[j + 1] = ordenada[j + 1], ordenada[j]

    alvo = input("Digite o código para pesquisa: ")
    try:
        alvo = int(alvo)
    except ValueError:
        print("Código não encontrado.")
        alvo = None
    if alvo is not None:
        ini, fim, achou = 0, len(ordenada) - 1, False
        while ini <= fim:
            meio = (ini + fim) // 2
            if ordenada[meio] == alvo:
                achou = True
                break
            if ordenada[meio] < alvo:
                ini = meio + 1
            else:
                fim = meio - 1
        if achou:
            print("Código encontrado.")
        else:
            print("Código não encontrado.")

    while len(fila) > 0:
        atual = fila.pop(0)
        processamento.append(atual)
        historico.append(atual)

    print("Lista ordenada:", ordenada)
    print("Ordem de processamento da fila:", processamento)
    if len(historico) == 0:
        print("Pilha vazia!")
    else:
        inverso = []
        while len(historico) > 0:
            inverso.append(historico.pop())
        print("Histórico em ordem inversa de processamento:", inverso)


