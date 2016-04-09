"""
Classe que modela um Quadrado com um atributo de lado
e os métodos de mudar/obter lado e calcular área
"""


class Quadrado(object):
    def __init__(self, lado=1):
        self.lado = lado

    def get_lado(self):
        return self.lado

    def set_lado(self, lado):
        self.lado = lado

    def get_area(self):
        return self.lado ** 2


if __name__ == '__main__':
    print('Digite o valor do lado do Quadrado')
    lado = int(input())

    quadrado = Quadrado(lado)

    print('Quadrado de lado =>', quadrado.get_lado())
    print('Quadrado de área =>', quadrado.get_area())
    quadrado.set_lado(4)
    print('Quadrado de lado =>', quadrado.lado)
    print('Quadrado de área =>', quadrado.get_area())
