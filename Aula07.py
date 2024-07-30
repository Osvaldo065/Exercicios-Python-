#Verificação de numero interio, par e impar

valor = int(input('Digite um número:'))

#Verificação do número digitado

if(valor%2)==0:
    print('O valor {} é um número par.'.format(valor))
elif(valor%2)!=0:
    print('O valor {} é um número impar.'.format(valor))
if(valor%10)==0:
    print('O valor {} é um número inteiro'.format(valor))
else:
    print('O valor {} não é um número inteiro.'.format(valor))
