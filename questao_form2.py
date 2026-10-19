fila = []
inicio = 0
qtd = 0

while True:
    entrada = input().split()

    if not entrada:
        continue

    op = entrada[0]

    if op == "0":
        break
    elif op == "1":
        fila.append(int(entrada[1]))
        qtd += 1
    elif op == "2":
        if qtd > 0:
            inicio += 1
            qtd -= 1
        else:
            print("Fila vazia")
    elif op == "3":
        if qtd > 0:
            print(fila[inicio])
        else:
            print("Próxima fila vazia")
    elif op == "4":
        print(qtd)
        
#Como funciona:
#1 X: adiciona no final com append() e aumenta qtd.
#2: em vez de remover da lista, avança o inicio em 1 e diminui qtd. O cliente atendido continua na lista, mas fica antes do índice inicio, então é ignorado.
#3: mostra fila[inicio] sem alterar nada.
#4: mostra qtd.
#2 ou 3 com qtd == 0: imprime a mensagem de fila vazia.

#Pela lógica da fila, esse é o resultado correto:
# os três 2 seguidos atendem 75 e 100 e depois tentam atender com a fila vazia, 
# e o 3 e o 4 finais consultam uma fila vazia.
# A saída do enunciado mostra um 100 e não mostra o 0 final,
# o que não bate com nenhuma regra descrita.
#Se o formulário comparar com a saída exata do enunciado,
