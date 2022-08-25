"""Crie um programa que leia uma frase qualquer e diga se aela é um palíndromo, desconsiderando espaços"""
f = str(input('Digite uma frase: ')).strip().upper()
p = f.split()  # separando palavra por palavra
j = ''.join(p)  # juntando a frase
i = '' # i = inverso
for l in range(len(j) - 1, -1, -1):
#  l = letra por letra
    i += j[l]
print(f'O inverso de {f.capitalize()} é {i}')
if i == j:
    print('Essa frase É um palíndromo!')
else:
    print('Essa frase NÃO é um palíndromo!')
