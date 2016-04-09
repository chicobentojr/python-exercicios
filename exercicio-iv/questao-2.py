"""
Classe derivada de lista que retorna somente os elementos sem repetição
"""


class MyList(list):
    def __init__(self, dados):
        list.__init__(self, dados)

    def get_itens(self):
        dados = []

        for x in self:
            if not x in dados:
                dados.append(x)
        return dados


if __name__ == '__main__':
    print('Digite os dados para serem inseridos na lista (separados por , [vírgula])')
    itens = list(input().split(','))

    print(MyList(itens).get_itens())
