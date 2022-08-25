'''Faça um programa que leia um número  de 0 a 9999 e mostre na tela cada um dos digitos separados.
ex: Digite um número: 1834 >>> Unidade: 4 - Dezena: 3 - Centena: 8 - Milhar: 1'''
n = int(input('Digite um nº de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

n = int(input('Digite um número de 0 a 9999: '))
nf = f'{n:>4}'
print(f'Unidade = {nf[3]}')
print(f'Dezena = {nf[2]}')
print(f'Centena= {nf[1]}')
print(f'Milhar = {nf[0]}')
