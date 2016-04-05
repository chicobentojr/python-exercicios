def dados_ordenados(dados, chave=0, reverso=False):
    """Esta função recebe uma lista de tuplas (dados),
    um inteiro (chave|padrõa 0 [zero]),
    um booleano (reverso|padrão False)
    e retorna os dados ordenados baseados nos
    outros parâmetros"""
    dados_retorno = []
    salto = -1 if reverso else 1
    quantidade = 0
    while quantidade != len(dados):
        item = dados[chave]
        dados_retorno.append(item)
        quantidade += 1
        chave += salto
        if chave == -1:
            chave = len(dados) - 1
        elif chave == len(dados):
            chave = 0
    return dados_retorno


lista_tupla = [(1, 2, 4),
               (2, 6, 3),
               (3, 6, 9),
               (1, 2),
               (36, 63, 31, 930)]

print('Lista original {0}'.format(lista_tupla))
print('Lista ordenada {0}'.format(dados_ordenados(lista_tupla, 2)))
print('Lista ordenada reversa {0}'.format(dados_ordenados(lista_tupla, 2, True)))
