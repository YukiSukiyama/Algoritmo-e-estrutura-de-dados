from collections import deque
import heapq

while True:
    try:
        N =int(input())
    except EOFError:
        break

    pilha = []
    fila = deque()
    prioridade = []

    epilha = True
    efila = True
    eprioridade = True

    for _ in range(N):
        operacao, valor = map(int, input().split())

        if operacao == 1:
            pilha.append(valor)
            fila.append(valor)
            heapq.heappush(prioridade, -valor)

        else:
            if not pilha:
                epilha = False
            else:
                removido = pilha.pop()

                if removido != valor:
                    epilha = False

            if not pilha:
                epilha = False
            else:
                removido = fila.popleft()

                if removido != valor:
                    epilha = False

            if not prioridade:
                eprioridade = False
            else:
                removido = -heapq.heappop(prioridade)

                if removido != valor:
                    eprioridade = False

    possibilidade = sum([
        epilha,
        efila,
        eprioridade
    ])

    if possibilidade == 0:
        print("impossible")
    elif possibilidade > 1:
        print("not sure")
    elif epilha:
        print("stack")
    elif efila:
        print("queue")
    else:
        print("priority queue")