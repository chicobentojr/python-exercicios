def comparar_pastas(caminho1, caminho2):
    """Esta função ler dois diretorios e retorna
    a lista de arquivos com nomes e/ou conteúdos diferentes"""

    from os import listdir
    from os.path import isfile, join

    arquivos1 = set([f for f in listdir(caminho1) if isfile(join(caminho1, f))])
    arquivos2 = set([f for f in listdir(caminho2) if isfile(join(caminho2, f))])

    arquivos = arquivos1.union(arquivos2)

    repeticoes = arquivos1.intersection(arquivos2)

    for item in repeticoes:
        texto1 = open(caminho1 + '/' + item).read()
        texto2 = open(caminho2 + '/' + item).read()

        if texto1 == texto2:
            arquivos.remove(item)

    return arquivos


if __name__ == '__main__':
    print('Digite o caminho dos diretórios (separados por , [vírgula])')
    c1, c2 = input().split(',')

    print(comparar_pastas(c1, c2))
