#Exercicio da calculadora

#função de adição
def soma(valorUm, valorDois):
    return valorUm + valorDois

#Função para subtrair
def subtracao(valorUm, valorDois):
    return valorUm - valorDois

#Função para multiplicar
def multiplicacao(valorUm, valorDois):
    return valorUm * valorDois

#Função para dividir 
def divisao(valorUm, valorDois):
    return valorUm / valorDois

#Função para ler os números digitados pelo usuário
def lerNum():
    lendo_Num = float(input('Digite um número:'))
    return lendo_Num

#Solicitando um valor ao usuário 
Lendo_Valor01 = lerNum()

#Exibindo opcao de calculo
opcao = int(input('Selecione a opção do calculo:\n \
[1] - Soma\n \
[2] - Subtração\n \
[3] - Multiplicação\n \
[4] - Divisão\n \
[5] - Sair\n'))


#Solicitando um valor ao usuário 
Lendo_Valor02 = lerNum()

# Utilizando o "Match case(switch)" 
# para fazer a verificação da opcao selecionada
match opcao:
    case 1:
        result = soma(Lendo_Valor01, Lendo_Valor02)
    case 2:
        result = subtracao(Lendo_Valor01, Lendo_Valor02)
    case 3:
        result = multiplicacao(Lendo_Valor01, Lendo_Valor02)
    case 4:
        result = divisao(Lendo_Valor01, Lendo_Valor02)
    case 5: 
        print('Saindo...')
    case _:
        print('Opção invalida.')

#Exibindo o resultado
print('O resultado é:\n R = {}'.format(result))






    