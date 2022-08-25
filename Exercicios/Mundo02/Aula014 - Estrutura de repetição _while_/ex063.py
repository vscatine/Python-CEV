"""Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8"""
print(f'\033[1;31m{" SEQUÊNCIA DE FIBONACCI ":~^50}\033[m')
n = int(input('Quantos números da sequência você quer ver? '))
t1 = 0
t2 = 1
t3 = t1 + t2
cont = 3
print(f'{t1} - {t2}', end=' - ')
while cont <= n:
    print(f'{t3}', end='')
    print(' - ', end='')
    cont += 1
    t1 = t2
    t2 = t3
    t3 = t1 + t2
print('FIM')
print(f'Sequência de Fibonacci finalizada com {cont - 1} números mostrados')
#  A baixo um exemplo visual da lógica, a primeira linha é que era,
#  a segunda a propria sequência de fibonacci
#  e a terceira os novos valores.
# t1  t2  t3
#  0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21 - 34 - 55
#      t1  t2  t3

"""Eu precisei ver a resolução do professor para poder sair do lugar. Esse é o código dele. 
Eu analisei e entendi a lógica, agora vou refazer sozinho para entender melhor. 23/02/2022 16:00"""

