def lista_dimensao(lista_comprimentos):
    """Esta função recebe uma lista de listas de comprimentos e retorna uma lista de uma dimensão"""

    dimensoes = []
    dimensao = 0

    for comprimentos in lista_comprimentos:
        for valor in comprimentos:
            dimensao += valor
        dimensoes.append(dimensao)
        dimensao = 0

    return dimensoes


comprimentos = [[1, 2, 3], [3, 6, 1]]

print('Comprimentos = {0}'.format(comprimentos))
print('Dimensões = {0}'.format(lista_dimensao(comprimentos)))
