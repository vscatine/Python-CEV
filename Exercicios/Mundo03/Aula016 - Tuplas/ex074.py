"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também o menor e maior valor da tupla."""
"""import random
maior = 0
menor = 101
n1 = random.randint(0, 100)
if n1 > maior:
    maior = n1
if n1 < menor:
    menor = n1
n2 = random.randint(0, 100)
if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2
n3 = random.randint(0, 100)
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3
n4 = random.randint(0, 100)
if n4 > maior:
    maior = n4
if n4 < menor:
    menor = n4
n5 = random.randint(0, 100)
if n5 > maior:
    maior = n5
if n5 < menor:
    menor = n5
tupla = (n1, n2, n3, n4, n5)
print(f'Os números sorteados foram: {tupla}\n'
      f'O maior valor sorteado foi {maior}\n'
      f'O menor valor sorteado foi {menor}')"""

# O programa funcionou, mas eu sinto que fiz uma gambiarra no menor e no sorteio. Como o exercício não delimita um
# número, eu usei um randint de 0 a 100, com o menor número recebendo 101 no começo, ou seja, qualquer número
# sorteado, vai ser menor que ele. De qualquer forma, vou ver a resolução do professor e verificar se tem como
# aprimorar, eu acredito que tenha. 03/03/2022 19:43
print('\nNOVO PROGRAMA')
from random import randint
n = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print('Os números sortedos foram: ', end='')
for e in n:
    print(f'{e}', end=' ')
print(f'\nO maior valor sorteado foi: {max(n)}')
print(f'O menor valor sorteado foi: {min(n)}')

# Vi a resolução do professor, e por mais que o meu programa tenha funcionado, eu não utilizei a tupla recurso
# principal. De qualquer forma, entendi a solução e já escrevi da forma correta. 07/03/2022  09:50
