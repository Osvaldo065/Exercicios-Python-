
#Função para receber o nome do usuário
def solicitar_nome_usario():
    nome_usuário = str(input("Digite seu nome:\n"))
    return nome_usuário

#Função solicitando o salario hora
def solicitar_salario_hora():
    print("Olá seja bem vindo!")
    salario_hora = float(input("Digite o seu salário hora:\n"))
    return salario_hora

#Função solicitando as horas trabalhadas 
def solicitar_horas_trabalhadas():
    horas_trabalhadas = float(input("Digite suas horas trabalhadas mensalmente:\n"))
    return horas_trabalhadas

#Função recebendo o percentual de desconto com base no salario informado
def solicitar_desconto_inss():
    desconto_inss = float(input("Digite o percentual de desconto com base no seu salário:\n"))
    return desconto_inss

#Função exibindo o salario bruto e o salario liquido do usuário
def exibir_salario ():

    nome_usario = solicitar_nome_usario()
    salario_hora = solicitar_salario_hora()
    horas_trabalhadas = solicitar_horas_trabalhadas()
    desconto_inss = solicitar_desconto_inss()

    #Calculando os valores e exibindo o total do salario bruto e liquido.
    salario_bruto = salario_hora*horas_trabalhadas
    print("{}, o seu salario bruto é: R${}".format(nome_usario, salario_bruto))
    
    salario_liquido = salario_bruto-(salario_bruto*desconto_inss/100)
    print("{}, o seu salario liquido é: R${}".format(nome_usario, salario_liquido))



exibir_salario()

