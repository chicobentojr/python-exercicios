def matrix_sum(*matrices):
    """Esta função retorna a soma das matrizes 2x2 recebidas nos parametros"""

    n1 = 0
    n2 = 0
    n3 = 0
    n4 = 0

    for matrix in matrices:
        n1 += matrix[0][0]
        n2 += matrix[0][1]
        n3 += matrix[1][0]
        n4 += matrix[1][1]

    return ([n1, n2],
            [n3, n4])


def camel_case(s):
    """Esta função retorna a string fornecida no formato CamelCase"""

    import re

    nome = ''

    rex = re.compile('\s+')

    for palavra in rex.split(s):
        nome += palavra[0].upper() + palavra[1:]

    return nome
