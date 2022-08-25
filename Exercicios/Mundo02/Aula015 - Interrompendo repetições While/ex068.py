"""Faça um programa que jogue PAR OU ÍMPAR com o jogador. O jogo só será interrompido quando o jogador PERDER,
mostrando o número total de vitórias consecutivas que ele conquistou no final do jogo."""
print(f'\033[1;33m{" VAMOS JOGAR PAR OU ÍMPAR ":~^40}\033[m')
print(f'\033[31m{"O jogo termina quando você perder":^40}\033[m')
from random import randint
cv = 0  # Contador de vitórias
cj = 0  # Contador de jogadas
while True:
    print('-' * 55)
    c = randint(0, 10)
    j = int(input('escolha um número de 0 a 10: '))
    while j < 0 or j > 10:
        print('\033[1;31mOpção inválida!\033[m Escolha um número entre 0 e 10')
        j = int(input('escolha um número de 0 a 10: '))
    pi = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    while pi not in 'PI':
        print('\033[1;31mOpção inválida!\033[m Escolha entre PAR ou ÍMPAR digitando P ou I')
        pi = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    soma = c + j
    cj += 1
    print(f'Você jogou {j} e o computador {c}. total de {soma}. ', end='')
    if soma == 0:
        print('\033[mzero é NEUTRO.\033[m')
    elif soma % 2 == 0:
        print('\033[1mDeu PAR.\033[m')
    else:
        print('\033[1mDeu ÍMPAR.\033[m')
    print('-' * 55)
    if soma == 0:
        print('\033[1;33mDeu EMPATE!\033[m')
    elif pi == 'P' and soma % 2 == 0 or pi == 'I' and soma % 2 != 0:
        cv += 1
        print('\033[1;32mVocê GANHOU!\033[m\n'
              'Vamos jogar novamente...')
    else:
        print('\033[1;31mVocê PERDEU!\033[m')
        print('-' * 55)
        break
if cv == 0:
    print('Você \033[1;31mnão ganhou nenhuma vez!\033[m HAHAHA')
elif cv == 1:
    print(f'Nós jogamos \033[1;36m{cj}\033[m vezes e você ganhou \033[1;32m{cv}\033[m vez')
else:
    print(f'Nós jogamos \033[1;36m{cj}\033[m vezes e você ganhou \033[1;32m{cv}\033[m vezes')

# Escrevi esse código soozinho, após ver o programa do professor rodando ainda no vídeo da aula, não vi a resoulção
# do exercício. Depois vou ver a resolução e ver se preciso alterar algo, mas no geral  gostei bastante do resultado
# final do meu programa. Não está permitindo que o jogador escolha um número fora de 0 - 10 e não deixa escolher
# outra coisa além de P ou I. Está verificando empates quando o jogador e o computador escolhem 0, já que zero não é
# par nem ímpar. Está dando mensagens finais com plural correto, caso o jogador ganhe apenas uma ou perca na primeira
# rodada. 28/02/2022 11:23
