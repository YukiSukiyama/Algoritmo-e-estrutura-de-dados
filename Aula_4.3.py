while True:
    try:
        N = int(input)
    except EOFError:
        break

    Telefones = []

    for _ in range(N):
        Telefones.append(input().strip())

        Telefones.sort()

        economia = 0

    for i in range (1, N):
        anterior = Telefones[i -1]
        atual = Telefones[i]

        J = 0
        while J < len(atual) and atual[J] == anterior[J]:
             J += 1 
             economia += J

    print(economia)
