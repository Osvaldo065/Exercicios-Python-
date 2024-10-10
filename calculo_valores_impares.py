
#metodo recebendo valores e fazendo a soma somente dos impares
def solicitarNum():
    valor = int(input("Digite um valor:\n"))
    
    somaImpares = 0 
    #Estrutura de respetição para verificar o valor digitado
    for i in range (valor):
        if (i%2) != 0: #Condicional para verificar se o número é impar
            somaImpares += i #soma dos números impares
    print(f"A soma dos números impares é: {somaImpares}")#exibindo a soma dos valores
            
#chamando o metodo para o main
solicitarNum() 
            

            