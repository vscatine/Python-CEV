"""Melhore o jogo do desafio 28 onde o computador vai 'pensar' em um número de 0 a 10. Só que agora o jogador
vai tentar adivinhar até acertar. Mostrando no final quantos palpites foram necessários para vencer."""
from random import randint
from time import sleep
print('Vou pensar em um número de 0 a 10, consegue adivinhar? ')
# sleep(2)
nc = randint(0, 10)  # Escolha do computador
nu = int(input('Em qual número eu pensei? '))  # Escolha do usuário
cp = 1  # contrador de palpites
if nu == nc:
    print('Você me venceu de primeira... PARABÉNS!')
while nu != nc:
    cp += 1
    nu = int(input('Você errou!\n'
                   'Vou te dar mais uma chance...\n'
                   'Em que número eu pensei? '))
if cp > 1:
    print(f'\nVocê conseguiu adivinhar em {cp} tentativas\nEu pensei no número {nc}')

# Escrevi esse código antes de ver a resolução do professor. Tá funcinando perfeitamente, só não coloquei cores e
# efeitos(sleep) vou ver a resolução, ver se tem algo a ser aprimorado, resscrever da forma do professor e talvez de
# uma forma mista, minha e do professor, colocando cores e etc 21/02/2022 13:58
