'''Crie um programa que leia o nome de uma pessoa e diga  se ela  tem "SILVA" no nome.'''
'''n = input('Digite seu nome completo: ').strip().upper()
#print(f'Você possuí "SILVA" no nome? {n.find("SILVA")}')
print(f'Você possuí "SILVA" no nome? {"SILVA" in n}')'''

n = input('Digite seu nome completo: ').strip()
s = 'SCATINE' in n.upper()
print(f'Seu nome possuí "Scatine"? {s}')
