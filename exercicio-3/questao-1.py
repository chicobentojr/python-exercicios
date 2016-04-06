def gen_primo():
    """
    Gerador de números primos
    """

    proximo = 0
    while True:
        cont = 0
        for num in range(1, proximo + 1):
            if proximo % num == 0:
                cont += 1
        if cont == 2:
            cont = 0
            yield proximo
            proximo += 1
        else:
            proximo += 1


if __name__ == '__main__':

    for n in gen_primo():
        print('Primo {0}'.format(n))
