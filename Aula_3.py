from collections import deque 

while True:
    N = int(input())

    if N == 0:
        break

    fila = deque(range(1, N+1))

    descartadas = []

    while len(fila) > 1:

            descartadas.append(str(fila.popleft()))

            fila.append(fila.popleft())
    print("Discarded cards:",",".join(descartadas))
    print("Remaining card:", fila[0])
    
    