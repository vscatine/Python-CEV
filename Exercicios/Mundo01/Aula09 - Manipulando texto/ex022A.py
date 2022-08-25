'''Crie um programa que leia o nome completo de uma  pessoa e mostre:
1 - O nome com todas as letras maiúsculas
2 - O nome com todas as letras minúsculas
3 - Quantas letras ao todo(sem considerar espaços)
4 - Quantas letras tem o primeiro nome'''
n = input('Nome Completo: ').strip()
print(f'Nome em maiúsculo: {n.upper()}')
print(f'Nome em minúsculo: {n.lower()}')
print(f'Seu nome tem {len(n) - n.count(" ")} letras')
#print(f'Seu primeiro nome tem {n.find(" ")} letras')
s = n.split()
print(f"""Seu primeiro nome é {s[0]} e ele tem {len(s[0])} letras
Seu segundo nome é {s[1]} e tem {len(s[1])} letras""")

