'''h) Escreva um programa para ler o nome e a idade de uma pessoa e imprimir o nome
e o valor que ela terá que pagar por um plano de saúde. O programa deverá levar em
consideração a tabela abaixo:
- até 10 anos - R$ 30,00
- acima de 10 até 29 anos - R$ 60,00
- acima de 29 até 45 anos - R$ 120,00
- acima de 45 até 59 anos - R$ 150,00
- acima de 59 até 65 anos - R$ 250,00

- acima de 65 anos - R$ 400,00.'''

#Função para receber o nome 
def solicitar_nome ():
    nome_cliente = str(input("Digite o seu nome:\n"))
    return nome_cliente

#Função para receber a idade do cliente
def solicitar_idade ():
    idade_cliente = int(input("\nDigite sua idade:\n"))
    return idade_cliente

#Função para realizar a verificação do plano de saúde
def valor_plano ():

    nome_cliente = solicitar_nome()
    idade_cliente = solicitar_idade()

    if idade_cliente <=10:
        print("{}, o valor do seu plano é R$30,00".format(nome_cliente))
    elif idade_cliente > 10 and idade_cliente <=29:
        print("{}, o valor do seu plano é R$60,00".format(nome_cliente))
    elif idade_cliente > 29 and idade_cliente <=45:
        print("{}, o valor do seu plano é R$120,00".format(nome_cliente))
    elif idade_cliente > 45 and idade_cliente <=59:
        print("{}, o valor do seu plano é R$150,00".format(nome_cliente))
    elif idade_cliente > 59 and idade_cliente <=65:
        print("{}, o valor do seu plano é R$250,00".format(nome_cliente))
    elif idade_cliente > 65:
        print("{}, o valor do seu plano é R$400,00".format(nome_cliente))

valor_plano()