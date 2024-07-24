# Calculando o IMC do usuário

#Função para solicitar os dados do usuário

def imc():
    nome = str(input('Digite seu nome:\n'))
    peso = float(input('Digite seu peso:\n'))
    altura = float(input('Digite sua altura:\n'))
    #Soma dos valores obtidos
    resultado_imc = peso/(altura*altura)
    print(nome,'o resultado do seu Imc é:{}'.format(resultado_imc))

    return resultado_imc


result_Imc = imc()

