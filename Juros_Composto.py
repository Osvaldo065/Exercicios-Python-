def valor_final_taxa():
#Recebendo o valor do investimento
    valor_investido = float(input('Digite o valor a ser investido:\n'))
    porcentagem_taxa_ano = 2.60 /100 #Definindo o valor da taxa divida por 100
#Selecionando a opçao 
    opcao_ano_investimento = int(input('Por quanto tempo você deseja investir?\n \
    [1] - 1 ano\n \
    [2] - 2 anos\n \
    [3] - 3 anos\n \
    [4] - 4 anos\n \
    [5] - + 5 anos\n '))
#Condicional verificando cada opção digitada
    if opcao_ano_investimento == 5:
        opcao_personalizada = int(input('Digite quanto tempo deseja investir:\n'))
        valor_final_investido = valor_investido*(1+porcentagem_taxa_ano)**opcao_personalizada
        print('O valor investido em {} anos é {:.2f}'.format(opcao_personalizada,valor_final_investido))
    elif opcao_ano_investimento == 1:
        valor_final_investido = valor_investido*(1+porcentagem_taxa_ano)**opcao_ano_investimento
        print('O valor investido em {} ano/s é {:.2f}'.format(opcao_ano_investimento,valor_final_investido))
    elif opcao_ano_investimento == 2:
        valor_final_investido = valor_investido*(1+porcentagem_taxa_ano)**opcao_ano_investimento
        print('O valor investido em {} ano/s é {:.2f}'.format(opcao_ano_investimento,valor_final_investido))
    elif opcao_ano_investimento == 3:
        valor_final_investido = valor_investido*(1+porcentagem_taxa_ano)**opcao_ano_investimento
        print('O valor investido em {} ano/s é {:.2f}'.format(opcao_ano_investimento,valor_final_investido))
    elif opcao_ano_investimento == 4:
        valor_final_investido = valor_investido*(1+porcentagem_taxa_ano)**opcao_ano_investimento
        print('O valor investido em {} ano/s é {:.2f}'.format(opcao_ano_investimento,valor_final_investido))
        
#Exibindo a função
valor_final_taxa()