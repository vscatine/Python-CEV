'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o  preço da passagem.
cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens com distâncias mais longas.'''
d = float(input('Distância da viagem em Km: '))
if d <= 200:
    print(f'O valor da sua passagem é R${d*0.50:.2f}')
else:
    print(f'O valor da sua passagem é R${d*0.45:.2f}')
