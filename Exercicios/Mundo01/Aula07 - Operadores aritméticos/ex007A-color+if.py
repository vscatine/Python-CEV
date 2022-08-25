#Desenvolva um programa que leia as duas notas e um aluno. Calcule e mostre a sua média.
'''a = input('Nome do aluno:')
n1 = float(input('Nota mensal'))
n2 = float(input('Nota Bimestral'))
m = (n1+n2)/2
print(f'O aluno(a) {a} tirou {n1} na prova mensal e {n2} na bimestral\nFicando com a média {m} no bimestre.')'''
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2) / 2
lc = {'g': '\033[1;32m',
      'r': '\033[1;31m',
      'cl': '\033[m'}
if n1 >= 6:
    print(f'Nota mensal: {lc["g"]}{n1}{lc["cl"]}')
else:
    print(f'Nota mensal: {lc["r"]}{n1}{lc["cl"]}')
if n2 >= 6:
    print(f'Nota bimestral: {lc["g"]}{n2}{lc["cl"]}')
else:
    print(f'Nota bimestral: {lc["r"]}{n2}{lc["cl"]}')
if m >= 6:
    print(f'\033[1;33mMédia\033[m: {lc["g"]}{m}{lc["cl"]}')
else:
    print(f'\033[1;33mMédia\033[m: {lc["r"]}{m}{lc["cl"]}')
