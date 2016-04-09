def ler_arquivo(nome):
    """Esta função recebe o nome do arquivo e
    retorna uma lista de tuplas com os dados
    separados por virgula"""
    try:
        import re

        lista_dados = []

        with open(nome, encoding='utf-8') as arquivo:

            rex = re.compile(',')

            for linha in arquivo:
                linha = linha.strip().strip('\n')
                if len(linha):
                    dados = rex.split(linha)
                    lista_dados.append(dados)

        return lista_dados
    except:
        return 'Aconteceu um erro na operação!'


if __name__ == '__main__':
    print('Digite o nome do arquivo para ser lido')
    arquivo = input()

    print(ler_arquivo(arquivo))
