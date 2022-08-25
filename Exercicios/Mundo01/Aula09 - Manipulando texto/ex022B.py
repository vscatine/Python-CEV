'''Crie um programa que leia o nome completo de uma  pessoa e mostre:
1 - O nome com todas as letras maiúsculas
2 - O nome com todas as letras minúsculas
3 - Quantas letras ao todo(sem considerar espaços)
4 - Quantas letras tem o primeiro nome'''
n = input('Nome Completo: ').strip()
s = n.split()
print(f'Seu nome em minúsculo é: {n.lower()}')
print(f'Seu nome em maiúsculo é: {n.upper()}')
print(f'Seu nome possuí {len(n) - n.count(" ")} letras.')
print(f'Seu primeiro nome é {s[0]} e possuí {len(s[0])}')

'''Estou refazendo os exercícios depois de assistir e ver todas as resoluções com o professor.'''
