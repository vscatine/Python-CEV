'''Faça um programa que leia um número inteiro e diga se é PAR ou ÍMPAR'''

'''import math
n = int(input(Digita um número: ))
p = math.'''

n = int(input('Digite um número: '))
r = n % 2
if r == 0:
    print(f'O número {n} é PAR')
else:
    print(f'O número {n} é ÍMPAR')
