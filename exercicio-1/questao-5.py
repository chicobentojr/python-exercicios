def inverter(frase):
    """Esta função recebe uma string como parâmetro e retorna suas palavras inversas"""
    nova_frase = ''
    for palavra in frase.split(' '):
        for letra in palavra[::-1]:
            nova_frase += letra
        nova_frase += ' '
    return nova_frase


f = input()

print(inverter(f))
