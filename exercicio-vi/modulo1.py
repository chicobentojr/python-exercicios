"""
Módulo com a função tribonacci(n) que retorna os
n elementos da sequência tribonacci
[Explicação da Sequência Tribonacci]
(https://programmingpraxis.com/2012/09/14/tribonacci-numbers/)
"""


def tribonacci(n):
    numeros = []
    a, b, c = 0, 0, 1

    for x in range(n):
        numeros.append(c)
        a, b, c = b, c, c + a + b

    return numeros


if __name__ == '__main__':
    print(tribonacci(10))
