'''Crie um programa que leia o nome completo de uma  pessoa e mostre:
1 - O nome com todas as letras maiúsculas
2 - O nome com todas as letras minúsculas
3 - Quantas letras ao todo(sem considerar espaços)
4 - Quantas letras tem o primeiro nome'''
n = input('Nome Completo: ')
u = n.upper()
l = n.lower()
c = n.strip()
s = n.split()

print(f'1 - {u}\n2 - {l}\n3 - {c}\n4 - {s.count([0])}')