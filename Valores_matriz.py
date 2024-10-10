# Método para verificar o menor valor da matriz
def retornar_menor(matriz):
    # Variável recebendo valor
    menor = matriz[0][0]
    # Estrutura de repetição para verificar o menor
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            # Condicional para verificar o menor número da matriz 
            if matriz[i][j] < menor:
                menor = matriz[i][j]
    return menor  # Retornando o menor valor
    
# Método para verificar o maior número da matriz 
def retornar_maior(matriz):
    # Variável maior recebendo o primeiro valor da matriz
    maior = matriz[0][0]
    # Estrutura de repetição para verificar o maior valor na matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            # Condicional verificando o maior valor
            if matriz[i][j] > maior:
                maior = matriz[i][j]
    return maior  # Retornando o maior valor da matriz
    
# Matriz recebendo os valores        
matriz = [
    [20, 15, 3],
    [14, 11, 4],
    [47, 21, 51]
]

# Exibindo o menor valor da matriz
print(f"O menor valor da matriz é: {retornar_menor(matriz)}")
# Exibindo o maior valor da matriz
print(f"O maior valor da matriz é: {retornar_maior(matriz)}")