N = int(input())

for _ in range(N):
    palavras = input().split()

    palavras.sort(key = len, reverse = True )

    print(" ".join(palavras))


