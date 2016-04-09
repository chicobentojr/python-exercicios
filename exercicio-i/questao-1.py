def celsius_para_fahrenheit(c):
    """Esta função recebe o valor do grau em Celsius e retorna seu valor convertido para Fahrenheit"""
    f = (9 / 5) * c + 32
    return f


def fahrenheit_para_celsius(f):
    """Esta função recebe o valor do grau em Fahrenheit e retorna seu valor convertido para Celsius"""
    c = (f - 32) / (9 * 5)
    return c


opcao = 'nenhuma'

while opcao:
    print('''Digite:
    C - para converter de Celsius para Fahrenheit
    F - para converter de Fahrenheit para Celsius
    0 - para sair da aplicação''')
    opcao = input()

    if opcao and opcao.upper() in ('C', 'F'):
        if opcao.upper() == 'C':
            print('Digite o valor em Celsius')
            valor = input()
        elif opcao.upper() == 'F':
            print('Digite o valor em Fahrenheit')
            valor = input()

        valor = float(valor)
        print('Valor fornecido', valor)
        print('Valor em Celsius', fahrenheit_para_celsius(valor))
        print('Valor em Fahrenheit', celsius_para_fahrenheit(valor))
        print()
    else:
        print('Digite um valor válido')
