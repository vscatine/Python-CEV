'''Faça um programa que leia o nome completo de uma pessoa. mostrando em seguida o primeiro e
o último nome separadamente.
Ex: Ana Maria de Souza >>> Primeiro: Ana - Último: Souza'''
n = input('Qual o seu nome completo? ').strip()
s = n.split()
print(f'Olá, {n}, prazer em conhce-lo!')
print(f'Seu primeiro nome é {s[0]}')
print(f'Seu último nome é {s[-1]}')
