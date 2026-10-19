if __name__ == "__main__":
    fila = []
    historico = []
    print("Digite os códigos dos chamados (-1 para encerrar):")
    while True:
        try:
            codigo = int(input("Código: "))
        except ValueError:
            print("Código inválido.")
            continue
        if codigo == -1:
            break
        if codigo < 0:
            print("Código inválido.")
            continue
        duplicado = False
        for i in range(len(fila)):
            if fila[i] == codigo:
                duplicado = True
                break
        if duplicado:
            print("Código duplicado; não foi inserido.")
        else:
            fila.append(codigo)
            print("Código adicionado.")

    while True:
        print("\n1 - Processar próximo chamado")
        print("2 - Consultar código")
        print("3 - Desfazer processamento")
        print("4 - Exibir fila atual")
        print("5 - Exibir histórico")
        print("0 - Encerrar")
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida.")
            continue

        if opcao == 1:
            if len(fila) == 0:
                print("Fila vazia.")
            else:
                codigo = fila[0]
                for i in range(1, len(fila)):
                    fila[i - 1] = fila[i]
                del fila[-1]
                historico.append(codigo)
                print(f"Chamado {codigo} processado e movido para o histórico.")

        elif opcao == 2:
            if len(fila) == 0:
                print("Fila vazia.")
            else:
                try:
                    alvo = int(input("Código para consultar: "))
                except ValueError:
                    print("Código inválido.")
                    continue
                copia = []
                for i in range(len(fila)):
                    copia.append(fila[i])
                for i in range(1, len(copia)):
                    chave = copia[i]
                    j = i - 1
                    while j >= 0 and copia[j] > chave:
                        copia[j + 1] = copia[j]
                        j -= 1
                    copia[j + 1] = chave
                esquerda = 0
                direita = len(copia) - 1
                encontrado = False
                while esquerda <= direita:
                    meio = (esquerda + direita) // 2
                    if copia[meio] == alvo:
                        encontrado = True
                        break
                    if alvo < copia[meio]:
                        direita = meio - 1
                    else:
                        esquerda = meio + 1
                if encontrado:
                    print("Código encontrado na fila.")
                else:
                    print("Código inexistente.")

        elif opcao == 3:
            if len(historico) == 0:
                print("Pilha vazia: não há histórico para desfazer.")
            else:
                codigo = historico[-1]
                del historico[-1]
                nova_fila = [codigo]
                for i in range(len(fila)):
                    nova_fila.append(fila[i])
                fila = nova_fila
                print(f"Desfazer: {codigo} retornou ao início da fila.")

        elif opcao == 4:
            if len(fila) == 0:
                print("Fila vazia.")
            else:
                print("Fila atual:", fila)

        elif opcao == 5:
            if len(historico) == 0:
                print("Pilha vazia: histórico vazio.")
            else:
                print("Histórico de processamento:", historico)

        elif opcao == 0:
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida.")