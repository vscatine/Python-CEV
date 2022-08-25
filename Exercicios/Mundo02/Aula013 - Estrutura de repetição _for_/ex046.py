"""Faça um programa que mostre na tela  uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 a 0, com um pasa de 1 segundo entre eles."""
from time import sleep
from emoji import emojize
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print(emojize('FELIZ ANO NOVO!!! :fireworks: :beer:', use_aliases=True))

