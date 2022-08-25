"""Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o  preço da passagem.
cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens com distâncias mais longas."""
from time import sleep
v = float(input('Distância da viagem em Km: '))
p1 = v * 0.50
p2 = v * 0.45
print('==*==*' * 10)
print('CALCULANDO')
sleep(0.77)
print('==*==*' * 10)
if v <= 200:
    print(f'O preço da sua passagem é R${p1:.2f}')
else:
    print(f'O preço da sua passagem é R${p2:.2f}')
