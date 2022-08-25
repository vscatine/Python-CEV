'''Crie um programa que leia o nome de uma pessoa e diga  se ela  tem "SILVA" no nome.'''
n = input('Nome Completo: ').strip()
print(f'Seu nome tem Silva? {"SILVA" in n.upper()}')

'''Solução apresentado pelo professor na resolução do exercício'''

n = input('Nome completo2: ').strip()
s = 'SILVA' in n.upper()
print(f'Seu nome tem "Silva"2? {s}')

'''Reescrevi utilizando variáveis ao invés de colocar as variáveis na string'''