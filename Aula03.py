#Comparando dois valores 

'''Estou utilizando uma função aqui para práticar'''

def valores():
    primeiro_valor = int(input('Digite um número:\n'))
    segundo_valor = int(input('\nDigite o segundo número:\n'))

    if (primeiro_valor > segundo_valor):
        print('\nO maior valor é: {}'.format(primeiro_valor))
    elif (segundo_valor > primeiro_valor):
        print('\nO maior valor é: {}'.format(segundo_valor))



comparacao_valores = valores()