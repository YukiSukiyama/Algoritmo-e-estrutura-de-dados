#questão 1
pilha = []

while True:
    entrada = input().split()

    if not entrada:
        continue

    op = entrada[0]

    if op == "0":
        break
    elif op == "1":
        pilha.append(int(entrada[1]))
    elif op == "2":
        if len(pilha) > 0:
            pilha.pop()
        else:
            print("Pilha vazia")
    elif op == "3":
        if len(pilha) > 0:
            print(pilha[-1])
        else:
            print("Pilha vazia")
#Como funciona:
#1 X: faz append(X), empilhando no topo.
#2: faz pop() para desfazer a última operação. Se a pilha estiver vazia, imprime “Pilha vazia” em vez de dar erro.
#3: mostra pilha[-1], o topo, sem remover nada. Se estiver vazia, imprime “Pilha vazia”.
#0: encerra o loop.
#O último 3 cai na pilha vazia, que é a quarta linha da saída esperada.
#Se o seu professor quiser que o 2 em pilha vazia não imprima nada,
#só trocar o print("Pilha vazia") dentro do elif op == "2" por pass.
#O enunciado só diz “tratar corretamente”, então vale conferir o que ele espera.