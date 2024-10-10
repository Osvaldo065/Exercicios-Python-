# Método para verificar a posição de um número dentro do vetor.
def encontra_numero(lista, numero):
    # Estrutura de repetição para verificar se o número está no vetor
    for i in range(len(lista)):
        # Condicional verificando se o número corresponde ao valor do índice
        if lista[i] == numero:
            return i  #Retornaremos a posição do numero 
            
    return -1 # Retornando -1 como mensagem quando nao estiver na lista

#Recebendo um valor digitado pelo usuario
valorNum = float(input("Digite um número para buscar no vetor: "))

# Testando a função
lista_numeros = [20, 5, 3, 7, 9, 10, 11, 6, 4, 8]
posicao = encontra_numero(lista_numeros, valorNum)

# Condicional para verificar e exibir o resultado
if posicao != -1:
    print(f"O número {valorNum} está na posição: {posicao}")
else:
    print(f"O número {valorNum} não está presente no vetor.")
