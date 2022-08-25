'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado.
a multa vai custar R$7.00 por cada km/h acima do limite.'''

v = float(input('Qual a velocidade atual do veículo? '))
m = (v - 80) * 7
if v > 80:
    print(f'MULTADO. Velocidade máxima na via 80km/h. Sua velocidade {v:3}km/h.\nVALOR DA MULTA: R${m:.2f}')
else:
    print('Transitando em velocidade segura.')
print('Tenha um bom dia, dirija com segurança!')