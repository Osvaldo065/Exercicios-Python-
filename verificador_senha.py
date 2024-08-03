def verificando_senha():
#Recebendo o nome do usuário e cadastrando senha
    user_name = str(input('Digite seu nome:'))
    cadastro_senha = str(input('\nCadastre uma senha:\n'))
    tentativas = 3 #Define a quantidade de tentativas
#Estrutura de repetição repetindo a solicitação da senha
    while tentativas > 0:
        print('\n{}, por gentileza'.format(user_name))
        senha_cadastrada = str(input('Digite sua senha:\n'))
        #Verificando se a senha digitada é diferente da senha cadastrada
        if senha_cadastrada != cadastro_senha:
            print('\nSenha incorreta, tente novamente!')
            tentativas -= 1 #Elimina uma tentativa a cada loop
            #Verificando se as tentativas chegaram a 0
            if tentativas == 0:
                print('\nO número de tentativas foi excedido')
        else:
            print('A senha está correta')
            break
#Exibindo a função
verificando_senha()