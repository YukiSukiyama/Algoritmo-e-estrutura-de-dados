casos = int(input())
for _ in range(casos):
    inicio = int(input())
    V, A = map(int, input().split())

    arestas = set()

    for _ in range(A):
        x, y = map(int, input().split())
        aresta = tuple(sorted((x, y)))  # Ordena os vértices para evitar duplicatas
        arestas.add(aresta)

    movimentos = len(arestas) * 2

    print(movimentos)
