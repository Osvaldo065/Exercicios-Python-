#Base para criar um jogo de palavras

''' Estou praticando o uso de funções'''
def encontre():

    nome = str(input('Digite seu nome:\n'))
    encontrar_letra = str(input('Digite o que deseja encontrar:\n'))

    #verificando o que o usuário digitou
    if(encontrar_letra in nome):
        print('{} está em {}'.format(encontrar_letra, nome))
    else:
        print('{} não está em {}'.format(encontrar_letra, nome))


verif_letra = encontre()