def info_arquivo_texto(arquivo_nome):
    """Esta função ler um arquivo texto e
    retorna a lista de palavras repetidas
    ordenadas pela quantidade de repetições"""

    lista_palavra = []

    with open(arquivo_nome, encoding='utf-8') as arquivo:
        for linha in arquivo:
            palavras = linha.strip().split(' ')
            for palavra in palavras:
                repeticao = False
                for item in lista_palavra:
                    if palavra == item[0]:
                        repeticao = True
                        item[1] += 1
                        break

                if not repeticao:
                    lista_palavra.append([palavra, 1])

    return lista_palavra


if __name__ == '__main__':
    print('Digite o nome do arquivo para ler')
    nome = input()

    lista = info_arquivo_texto(nome)

    print(sorted(lista, key=lambda i: i[1], reverse=True))
