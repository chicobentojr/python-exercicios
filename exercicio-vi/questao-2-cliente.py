# questão não testada e baseada no código do livro

"""
Cliente que obtém um objeto utilizador da função tribonacci(n)
"""

import Pyro.core

if __name__ == '__main__':

    proxy = Pyro.core.getProxyForURI('PYROLOC://127.0.0.1/tribonacci')

    print(proxy.calcular(10))