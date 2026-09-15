N = int(input())

for _ in range(N):
    texto = input()
    resultado = []
    i = 0

    while i < len(texto):
        if texto[i] == "0":
            inicio = i

            while i < len(texto) and texto[i] == "0":
                i += 1
            quantidade = i - inicio

            if quantidade >= 3:
                while quantidade > 255:
                    resultado.append('#')
                    resultado.append(chr(255))

                    quantidade -= 255
                resultado.append('#')
                resultado.append(chr(quantidade))
            else:
                resultado.append('0' * quantidade )
        #Referente aos espaços
        elif texto[i] == "":
            inicio = i

            while i < len(texto) and texto[i] == "0":
                i += 1
            quantidade = i - inicio

            if quantidade >= 3:
                while quantidade > 255:
                    resultado.append('$')
                    resultado.append(chr(255))

                    quantidade -= 255
                resultado.append('$')
                resultado.append(chr(quantidade))
            else:
                resultado.append('0' * quantidade )
        else:
            resultado.append(texto[i])
            i += 1
    print(''.join(resultado))
            