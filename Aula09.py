#Exercicio de comparação de tamanho do nome digitado

user_name = input('Digite seu nome:')

#Variavel recebendo a quantidade de letras digitadas

qtd_letras = len(user_name)

#Condicional verificando e comparando a quantidade de letras

if (qtd_letras>=1 and qtd_letras<=4):
    print('O nome {} é curto.'.format(user_name))
elif(qtd_letras<=7 and qtd_letras>=5):
    print('O nome {} é normal.'.format(user_name))
elif(qtd_letras>7):
    print('O nome {} é grande.'.format(user_name))
    