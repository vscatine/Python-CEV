"""Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50"""
print('Os números pares entre 1 e 50  são:')
from time import sleep
sleep(1)
for pi in range(1, 51):
    r = pi % 2
    if r == 0:
        sleep(0.25)
        print(pi)

# escrevi revendo o exercício de par ou impar, agora vou reescrever depois te der visto a resolução do professor.
