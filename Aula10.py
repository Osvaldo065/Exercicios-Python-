#Exercicio com estrutura de repetição

user_name = input('Digite seu nome:')

qtd_letras = len(user_name)
indice = 0
novo_nome = ''
#Estrutura de repetição para contar as letras e exibir cada iteração com '*'

while indice < qtd_letras:
   letra = user_name[indice]
   novo_nome += f'+(letra)'
   indice += 1

print(novo_nome)

