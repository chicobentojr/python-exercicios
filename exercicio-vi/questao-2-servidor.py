# questão não testada e baseada no código do livro

"""
Servidor que publica um objeto utilizador da função tribonacci(n)
"""

import Pyro.core
import modulo1


class Tribonacci(Pyro.core.ObjBase):
    def calcular(self, n):
        return modulo1.tribonacci(n)


if __name__ == '__main__':
    Pyro.core.initServer()

    daemon = Pyro.core.Daemon()

    uri = daemon.connect(Tribonacci(), 'tribonacci')

    daemon.requestLoop()
