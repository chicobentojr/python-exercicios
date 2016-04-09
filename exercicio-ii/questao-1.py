def criar_arquivo(nome):
    """Esta função cria um arquivo de texto fixo
    com o nome recebido no parametro"""
    texto = 'Este é um texto\naleatório\npara testar um tutorial\nde Python'

    with open(nome, 'w', encoding='utf-8-sig') as arquivo:
        arquivo.write(texto)


def info(arquivo_nome):
    """Esta função recebe o nome do arquivo e retorna:
    número de caracteres,te
    número de linhas e
    núnero de palavras
    """
    import re

    with open(arquivo_nome, encoding='utf-8') as arquivo:
        caracteres = 0
        palavras = 0
        linhas = 0
        for linha in arquivo:
            linhas += 1

            caracteres += len(linha)
            rex = re.compile('\w+')

            palavras += len(rex.findall(linha))

        print('Quantidade de Caracteres -> {0}'.format(caracteres))
        print('Quantidade de Linhas -> {0}'.format(linhas))
        print('Quantidade de Palavras -> {0}'.format(palavras))


if __name__ == '__main__':
    print('Digite o nome do arquivo...')
    nome_arquivo = input()

    criar_arquivo(nome_arquivo)

    info(nome_arquivo)
