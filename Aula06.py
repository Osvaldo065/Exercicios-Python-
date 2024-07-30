#Exercicio velocidade do carro

velocidade = 61
quilometros = 90 

#Constantes
RADAR_1 = 60
QUILOMETROS = 100
RADAR_RANGE = 1


#Condicional para verificar a velocidade do carro

if velocidade > RADAR_1:
    print('Velocidade do carro passou do radar 1')

if quilometros >= (QUILOMETROS-RADAR_RANGE) and quilometros <= (QUILOMETROS + RADAR_RANGE):
    velocidade > RADAR_1
    print('Carro multado no radar 1')
