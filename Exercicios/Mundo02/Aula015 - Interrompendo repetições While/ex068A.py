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
    j = -1
    while j < 0 or j > 10:
        j = int(input('escolha um número de 0 a 10: '))
    pi = ' '
    while pi not in 'PI':
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

# Vi a resolução do professor e de tudo que ele fez no código, eu alterei somente a inserção do par ou impar e do
# número do jogador, mas mesmo assim ainda prefiro a forma como eu fiz, pq no dele, não aparece a mensagem de erro
# para o usuário. Eu entendi a lógica de tratamento de vitória e derrota dele, mas ainda preferi a minha,
# que fica mais fácil de tratar o zero como neutro (empate) e acaba "gastando" menos linhas. No geral meu código
# ficou maior que o dele, mas, eu estou tratando mais coisas, como empate, mensagem caso vença só uma vez no
# singular, caso não vença nenhuma vez, e se vencer mais de uma, no plural, entre outras coisas.
# No fim das contas, gostei bastante do meu resultado! 02/03/2022 11:55
