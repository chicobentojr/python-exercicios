import modulo2

print('Criando Matrizes...')

m1 = ([2, 2],
      [4, 6])

print('Matriz m1 criada => {0}'.format(m1))

m2 = ([-3, 4],
      [2, -2])

print('Matriz m2 criada => {0}'.format(m2))

print('Soma das matrizes => {0}'.format(modulo2.matrix_sum(m1, m2)))

print('\nDigite um nome para ser convertido')

nome = input()

print('Nome convertido para CamelCase => {0}'.format(modulo2.camel_case(nome)))
