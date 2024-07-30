#Exercicio do horário

#Importando biblioteca para puxar o horário atual.

import datetime

#Variavel recebe horario atual
hora_atual = datetime.datetime.now()
hora = hora_atual.hour
#Solicitando o nome do usuário
user_name = input('Digite seu nome:')

#Verificando o horário e exibindo a saudação com base no horário

if (hora >= 0 and hora <= 11):
    print('{}, tenha um bom dia!'.format(user_name))
elif( hora >= 12 and hora <= 17):
    print('{}, tenha uma boa tarde!'.format(user_name))
elif(hora >= 18 and hora <= 23):
    print('{}, tenha uma boa noite!'.format(user_name))

#Exibindo o horário

print('Horário atual: {}'.format(hora_atual.strftime("%H:%M:%S")))