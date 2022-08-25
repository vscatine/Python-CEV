'''Faça um programa que leia o nome completo de uma pessoa. mostrando em seguida o primeiro e
o último nome separadamente.
Ex: Ana Maria de Souza >>> Primeiro: Ana - Último: Souza'''
n = input('Qual o seu nome completo? ').strip().title()
print(f'Olá, {n}, prazer em te conhecer!')
print(f'Seu primeiro nome é {n.split()[0]}')
print(f'Seu último nome é {n.split()[-1]}')


