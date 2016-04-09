def obter_dados(dicionario):
    """Esta função recebe um dicionário e retorna a soma, média e variação dos valores"""
    soma = 0
    maior = 0
    menor = list(dicionario.values())[0]
    for valor in dicionario.values():
        soma += valor
        maior = valor if valor > maior else maior
        menor = valor if valor < menor else menor

    media = soma / len(dicionario)
    variacao = maior - menor
    return soma, media, variacao


dicio = {"a": 1,
         "b": 5,
         "c": 9,
         "d": 5}

soma, media, variacao = obter_dados(dicio)

print(
    '''Soma = {0}\nMédia = {1}\nVariação = {2}
      '''.format(soma, media, variacao))
