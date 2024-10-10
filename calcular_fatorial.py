
#Metodo para receber um valor e calcular o fatorial dele
def solicitarValor():
    #variavel recebendo um valor
    valor = int(input("Digite um valor:"))
    #variavel recebendo valor
    fatorialNum = 1
    #Estrutura de repetição para realizar o calculo do fatorial
    for i in range(2,valor + 1):
        fatorialNum *= i #realizando a multiplicação do valor 
    return fatorialNum #retornando o valor final

#variavel recebendo valor chamando a função para o main
resultado = solicitarValor()
print(f"O valor do fatorial é: {resultado}")