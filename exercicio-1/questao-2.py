def e_primo(valor):
    """Esta função recebe um valor inteiro e retorna verdadeiro caso o valor seja primo e falso caso contrário"""
    cont = 0
    for num in range(1, valor + 1):
        cont = cont + 1 if valor % num == 0 else cont
    return cont == 2


for num in range(1, 101):
    print('{0} é primo? {1}'.format(num, e_primo(num)))
