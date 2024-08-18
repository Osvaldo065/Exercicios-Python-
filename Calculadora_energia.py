
#Função para solicitar o nome do consumidor
def solicitar_nome ():
    nome_cliente = str(input("Digite seu nome\n"))
    return nome_cliente
#Função do menu de opção
def menu_opcao_consumidor():
    print("Selecione a opção correspondente ao seu perfil:\n")
    return int(input("[1]-Residência\n\
    [2]-Comércio\n\
    [3]-Indústria\n\
    [4]-Sair\n"))

#Função para receber os valores consumidos por Kw/h
def receber_consumo():
    consumo_energia = float(input("Digite o consumo em kw/h:\n"))
    return consumo_energia
#Função para calcular a conta de energia do cliente
def calcular_conta_cliente():
    #Variaveis recebendo os valores das taxas por Kw/h
    residencia = 0.60
    comercio = 0.48
    industria = 1.29
    taxa_iluminacao_publica = 20
    bandeira_vermelha = 4
    #variavel recebendo a função de escolha
    nome_cliente = solicitar_nome()
    opcao_selecionada = menu_opcao_consumidor()
    consumo_cliente = receber_consumo()
    #condição para verificar a opcao selecionada e calular os valores
    if opcao_selecionada == 1:
        fatura_energia = (consumo_cliente*0.60)+taxa_iluminacao_publica+bandeira_vermelha
        print("{}, sua fautra mensal é: R${}".format(nome_cliente, fatura_energia))
    elif opcao_selecionada == 2:
        fatura_energia = (consumo_cliente*0.48)+taxa_iluminacao_publica+bandeira_vermelha
        print("{}, sua fautra mensal é: R${}".format(nome_cliente, fatura_energia))
    elif opcao_selecionada == 3:
        fatura_energia = (consumo_cliente*1.29)+taxa_iluminacao_publica+bandeira_vermelha
        print("{}, sua fautra mensal é: R${}".format(nome_cliente, fatura_energia))
    elif opcao_selecionada == 4:
        print("Saindo...")

calcular_conta_cliente()
