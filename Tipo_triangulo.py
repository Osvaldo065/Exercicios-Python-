#metodo para verificar os tipos de triangulos
def tipo_triangulo(lado1, lado2, lado3):
    # Verifica se o triângulo é válido
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        # Triângulo válido
        if lado1 == lado2 == lado3:
            return "Equilátero"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "Isósceles"
        else:
            return "Escaleno"
    else:
        return "Triângulo inválido"

# Recebendo os valores dos lados do triangulo
lado1 = float(input("Digite o primeiro lado do triângulo:\n"))
lado2 = float(input("\nDigite o segundo lado do triângulo:\n "))
lado3 = float(input("\nDigite o terceiro lado do triângulo:\n "))

#Variavel resultado chamado a função e seus parametros para o main 
resultado = tipo_triangulo(lado1, lado2, lado3)
#Exibindo o resultado para o usuário
print(f"O triângulo é: {resultado}")

