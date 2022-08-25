'''Escreva um programa que faça o computador "pensar" em um número inteiro de 0 a 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador. o programa deverá escrever na tela se o usuário
venceu ou perdeu.'''
print('Olá, vou pensar em um numero inteiro de 0 a 5 consegue adivinhar qual o número?')
nu = int(input('Qual número eu pensei? '))
import random
nc = random.randint(0,5)
if nc == nu:
    print(f'Pensei no número {nc:1} VOCÊ GANHOU!')
else:
    print(f'Pensei no numero {nc:1} VOCÊ PERDEU')
