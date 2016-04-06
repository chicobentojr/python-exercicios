def split(fn, n):
    """Esta função divide o arquivo fn em partes de n bytes e
    gera as partes com o seguinte padrão:
    Ex.: arq.txt -> arq_001.txt, arq_002.txt"""

    contador = 1
    parte = []

    nome, extensao = tuple(fn.name.split('.'))

    with open(fn.name, 'rb') as arquivo:
        bytes = arquivo.read()
        index = 0
        for byte in bytes:
            parte.append(byte)

            if len(parte) == n or index == len(bytes) - 1:
                parte_nome = nome + ('_%03d' % contador) + '.' + extensao
                trecho = open(parte_nome, 'wb')
                trecho.write(bytearray(parte))
                trecho.close()
                print('Parte {0} criada com sucesso!'.format(parte_nome))
                contador += 1
                parte = []
            index += 1


def join(fn, fnlist):
    """Esta função junta os arquivos de fnlist e põe  no arquivo fn"""

    bytes = []

    for item in fnlist:
        with open(item, 'rb') as arquivo:
            bits = arquivo.read()
            for bit in bits:
                bytes.append(bit)

    with open(fn, 'wb') as novo_arquivo:
        novo_arquivo.write(bytearray(bytes))
