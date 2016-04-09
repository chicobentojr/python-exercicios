"""
Classe Carro
"""


class Carro(object):
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0.0

    def mover(self, km):
        self.combustivel -= float(km / self.consumo)

    def gasolina(self):
        return self.combustivel

    def abastecer(self, litros):
        self.combustivel += litros


if __name__ == '__main__':
    print('Digite o valor de consumo do Carro')
    carro = Carro(int(input()))
    print('Digite um valor de litros para abastecer seu carro')
    carro.abastecer(float(input()))
    print('Digite quantos km seu carro percorreu')
    carro.mover(float(input()))
    print('Seu carro ainda tem {0} litro(s) de gasolina'.format(carro.gasolina()))
