"""Crie um programa que faça o computador jogar JOKENPO com você."""
from random import randint
from time import sleep
lc = {'cl': '\033[m',
    'yg': '\033[1;33;40m',
    'yb': '\033[1;33m',
    'gb': '\033[1;32m',
    'rb': '\033[1;31m',
    'mb': '\033[1;35m',
    'cb': '\033[1;36m'}
print(f'{lc["yb"]}-=-{lc["cl"]}' * 10)
print(f'{lc["yg"]}CONSEGUE ME VENCER NO JOKENPÔ?{lc["cl"]}')
print(f'{lc["yb"]}-=-{lc["cl"]}' * 10)
sleep(2)
l = (f'{lc["rb"]}PEDRA{lc["cl"]}', f'{lc["mb"]}PAPEL{lc["cl"]}', f'{lc["cb"]}TESOURA{lc["cl"]}')
c = randint(0, 2)
j = int(input(f'Suas opções:\n'
              f'[ 0 ] {l[0]}\n'
              f'[ 1 ] {l[1]}\n'
              f'[ 2 ] {l[2]}\n'
              'Qual é sua jogada? '))
if j not in (0, 1, 2):
    print(f'{lc["rb"]}JOGADA INVÁLIDA{lc["cl"]}\nTente novamente escolhendo entre \033[1m0, 1 ou 2\033[m')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print(f'{lc["yb"]}-=-{lc["cl"]}' * 10)
    print(f'O Computador jogou: {l[c]}\n'
          f'Você jogou: {l[j]}')
    print(f'{lc["yb"]}-=-{lc["cl"]}' * 10)
    if c == 0: # Computador jogou PEDRA
        if j == 0:
            print(f'{lc["yb"]}EMPATE!{lc["cl"]}')
        elif j == 1:
            print(f'{lc["gb"]}VOCÊ GANHOU!{lc["cl"]}')
        elif j == 2:
            print(f'{lc["rb"]}VOCÊ PERDEU!{lc["cl"]}')
    elif c == 1: # Computador jogou PAPEL
        if j == 0:
            print(f'{lc["rb"]}VOCÊ PERDEU{lc["cl"]}')
        elif j == 1:
            print(f'{lc["yb"]}EMPATE!{lc["cl"]}')
        elif j == 2:
            print(f'{lc["gb"]}VOCÊ GANHOU!{lc["cl"]}')
    elif c == 2: # Computador jogou TESOURA
        if j == 0:
            print(f'{lc["gb"]}VOCÊ GANHOU!{lc["cl"]}')
        elif j == 1:
            print(f'{lc["rb"]}VOCÊ PERDEU{lc["cl"]}')
        elif j == 2:
            print(f'{lc["yb"]}EMPATE!{lc["cl"]}')
# Eu copiei e colei, pq já escrevi duas vezes a base desse programa, dessa vez eu só alterei os ifs, deixando igual o o professor
# Não gostei muito dessa forma, preferi a forma como eu escrevi, mesmo assim, achei bom dexiar registrado essa outra forma. 15/02/2022 17:31
