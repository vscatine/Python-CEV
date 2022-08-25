'''Faça um programa que leia o nome completo de uma pessoa. mostrando em seguida o primeiro e
o último nome separadamente.
Ex: Ana Maria de Souza >>> Primeiro: Ana - Último: Souza'''
n = input('Nome completo: ').strip()
ns = n.split()
print(f'Primeiro nome: {ns[0]}\nÚltimo nome: {ns[2]}')

n = input('Nome Completo2: ').strip().split()
print(f'Olá, {n}!')
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu último nome é {n[2]}')
