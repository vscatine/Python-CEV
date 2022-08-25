"""Crie um programa que faça o computador jogar JOKENPO com você."""
from random import randint
from time import sleep

print('CONSEGUE ME VENCER NO JOKENPO?')
c = randint(1, 3)
print('Suas opções:\n'
      '[ 1 ] PEDRA\n'
      '[ 2 ] PAPEL\n'
      '[ 3 ] TESOURA')
j = int(input('Qual é sua jogada? '))
if j not in (1, 2, 3):
    print('OPÇÃO INVÁIDA! tente novamente. ')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(0.2)
    print('-=-' * 13)
    print(f'Computador jogou: {c}\n'
          f'Jogador jogou: {j}')
    print('-=-' * 13)
    if c == j:
        print('EMPATE!')
    elif c == 1 and j == 3 or c == 2 and j == 1 or c == 3 and j == 2:
        print('VOCÊ PERDEU!')
    elif j == 1 and c == 3 or j == 2 and c == 1 or j == 3 and c == 2:
        print('VOCÊ VENCEU!')
# Escrevi antes de ver a a resolução do exercício pelo professor e não sabia como fazer o programa
# printar os números como PEDRA, PAPEL E TESOURA. Mesmo assim, ainda gostei mais da minha solução do que a do professor
# vou reescrever alterando 1, 2, 3 por pedra papel e tesoura e colocando cor. 15/02/2022 15:40
