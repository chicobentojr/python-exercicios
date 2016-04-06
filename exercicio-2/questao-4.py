import modulo4

if __name__ == '__main__':
    print('Digite o nome do arquivo que você quer dividir')
    arquivo = input()
    print('Forneça quantos bytes você quer para cada parte')
    quant = int(input())

    with open(arquivo) as a:
        modulo4.split(a, quant)

    print()
    print('Digite a lista de arquivos que você quer unir (separados por , [vírgula])')
    lista = input().split(',')
    print('Digite o nome do arquivo que você quer gerar com essa união')
    novo_arquivo = input().strip()

    modulo4.join(novo_arquivo, lista)

    print('Arquivo gerado com sucesso!')
