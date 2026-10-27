class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None 

def inserir(raiz, valor):
    if raiz is None:
        return No(valor)
    if valor < raiz.valor:
        raiz.esquerda = inserir(raiz.esquerda, valor)
    elif valor > raiz.valor:
        raiz.direita = inserir(raiz.direita, valor)
    return raiz

def pre_ordem(raiz, resultado):
    if raiz is not None:
        resultado.append(str(raiz.valor))
        pre_ordem(raiz.esquerda, resultado)
        pre_ordem(raiz.direita, resultado)

def em_ordem(raiz, resultado):
    if raiz is not None:
        em_ordem(raiz.esquerda, resultado)
        em_ordem(raiz.direita, resultado)

def pos_ordem(raiz, resultado):
    if raiz is not None:
        pos_ordem(raiz.esquerda, resultado)
        pos_ordem(raiz.direita, resultado)
        resultado.append(str(raiz.valor))

casos = int(input())

for caso in range(1, casos + 1):
    N = int(input())
    valores = list(map(int, input().split()))
    raiz = None
    for valor in valores:
        raiz = inserir(raiz, valor)

    pre = []
    inf = []
    pos = []

    pre_ordem(raiz, pre)
    em_ordem(raiz, inf)
    pos_ordem(raiz, pos)

    print(f"Case {caso}:")
    print("Pre.:"+ " ".join(pre))
    print("In..:"+ " ".join(inf))
    print("Post:"+ " ".join(pos))
    print()
