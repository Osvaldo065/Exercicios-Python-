'''Faça um algoritmo que calcule o volume de caixa uma dágua cilíndrica, sendo que
o raio e a altura devem ser fornecidos (lidos pelo teclado).
Formula: V = PI * Raio^2 * Altura'''

#Função recebendo os valos do Raio
def solicitar_raio ():
    raio = float(input("Informe o valor do raio:\n"))
    return raio

#Função para receber a altura
def solcitar_altura ():
    altura = float(input("\nInforme o valor da altura:\n"))
    return altura

#Função para realizar o calculo
def calcular_volume ():
    import math 
    valor_raio = solicitar_raio()
    valor_altura = solcitar_altura()
    pi = math.pi
    valor_volume = pi*(valor_raio**2*valor_altura)
    print("O valor do volume d_água é: {}". format(valor_volume))

calcular_volume()