import time


def gen_rgb_cores():
    """
    Gerador de cores RGB
    """

    for r in range(256):
        for g in range(256):
            for b in range(256):
                yield (r, g, b)


def rgb_cores():
    """
    Função que retorna tuplas de cores RGB
    """
    cores = []
    for r in list(range(256)):
        for g in list(range(256)):
            for b in list(range(256)):
                cores.append((r, g, b))
    return cores


if __name__ == '__main__':

    start = time.time()
    for i in gen_rgb_cores():
        pass
    end = time.time()
    print('Tempo usando gerador: {0}'.format(end - start))

    start = time.time()
    a = rgb_cores()
    end = time.time()
    print('Tempo usando função: {0}'.format(end - start))
