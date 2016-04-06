import re


def gen_ler_arquivo(nome):
    """
    Este Gerador recebe o nome do arquivo e
    retorna uma lista de tuplas com os dados
    separados por virgula
    """
    try:

        with open(nome, encoding='utf-8') as arquivo:

            rex = re.compile(',')

            for linha in arquivo:
                linha = linha.strip().strip('\n')
                if len(linha):
                    dados = rex.split(linha)
                    yield dados
    except:
        return 'Aconteceu um erro na operação!'


if __name__ == '__main__':
    print('Digite o nome do arquivo para ser lido')
    arquivo = input()

    for tupla in gen_ler_arquivo(arquivo):
        print(tupla)
