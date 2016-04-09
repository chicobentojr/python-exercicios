"""
Classe Animal para operações usando pickle
"""
import pickle


class Animal(object):
    def __init__(self):
        self.nome = ''
        self.especie = ''
        self.genero = ''
        self.peso = 0.0
        self.altura = 0.0
        self.idade = 0

    def salvar(self):
        pickle.dump(self, open('animal.pkl', 'wb'))

    def desfazer(self):
        dado = pickle.load(open('animal.pkl', 'rb'))
        self.nome = dado.nome
        self.especie = dado.especie
        self.genero = dado.genero
        self.peso = dado.peso
        self.altura = dado.altura
        self.idade = dado.idade


if __name__ == '__main__':
    animal = Animal()

    animal.nome = 'Cadu'
    animal.especie = 'Canis Lupus'
    animal.genero = 'Canis'
    animal.peso = 13.3
    animal.altura = 36
    animal.idade = 6

    animal.salvar()
    print(animal.nome)
    animal.nome = "Carlos Eduardo"
    print(animal.nome)
    animal.desfazer()
    print(animal.nome)
