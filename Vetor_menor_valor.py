
#Metodo para retornar o menor numero dentro do vetor.
def retorna_menor_numero(lista):#Paramentro lista
    menor = lista[0] #Variavel recebendo o valor
    #Estrutura de repetição para contar e verificar o menor valor.
    for i in range(1, len(lista)):
        #Condicional verificando os indices 
        if lista[i] < menor:
            #Variavel menor recebendo o valor do indice
            menor = lista[i]
    return menor

# Testando a função e exibindo o menor valor.
print(f" O menor valor dentro do vetor é: {retorna_menor_numero([20, 5, 3, 7, 9, 10, 11, 6, 4, 8])}")

