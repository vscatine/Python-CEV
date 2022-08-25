"""Crie um programa que leia uma frase qualquer e diga se aela é um palíndromo, desconsiderando espaços"""
f = str(input('Digite uma frase: ')).strip().upper().split()
j = ''.join(f)
i = ''
for l in range(len(j) - 1, -1, -1):
    i = i + j[l]
print(f'O inverso de {j} é {i}')
if i == j:
    print('E é um palíndromo!')
