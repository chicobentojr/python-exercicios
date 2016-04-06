"""
    Gerador de números primos usando itertools
"""
import itertools


def e_primo(valor):
    if valor == 1:
        return False
    for num in range(2, valor + 1):
        if not num == 1 and not num == valor and valor % num == 0:
            return False
    return True


if __name__ == '__main__':

    gen_primo = (n for n in itertools.count() if e_primo(n))

    for n in gen_primo:
        print('Primo {0}'.format(n))
