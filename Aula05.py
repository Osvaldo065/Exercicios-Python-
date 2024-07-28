#Exercicio de manipulação de string

nome = input('Digite seu nome:')
idade = input('Digite sua idade:\n')
#Exibindo o nome e invertendo
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
#Verificando se o nome tem espaços
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços.')

#Contando a quantidade de letras

    print(f'\nSeu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
else:
    print('Desculpe, você não preencheu os campos.')







    


