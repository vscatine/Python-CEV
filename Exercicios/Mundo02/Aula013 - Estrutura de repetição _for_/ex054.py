"""Crie um programa que leia o ANO DE NASCIMENTO de sete pessoas. No final, mostre quantas pessoas ainda
não antigiram a maioridade e quantas já são maiores. """
from datetime import date
contp = 0  # contp (contagem "plus", maiores de idade)
contm = 0  # contm (contagem menores de idade)
for c in range(0, 7):
    an = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    at = date.today().year  # at = ano atual
    if at - an >= 18:
        contp += 1
    else:
        contm += 1
if contp == 0:
    print('\n\033[1;30;41mATENÇÃO!!! TODOS SÃO MENORES DE IDADE! \033[m')
elif contm == 0:
    print('\n\033[1;97;42mTODOS SÃO MAIORES DE IDADE! \033[m')
else:
    if contp == 1:
        print(f'\nTemos \033[1;32m{contp}\033[m pessoa maior de idade\n'
              f'E \033[1;31m{contm}\033[m pessoas menores de idade')
    elif contm == 1:
        print(f'\nTemos \033[1;32m{contp}\033[m pessoas maiores de idade\n'
              f'E \033[1;31m{contm}\033[m pessoa menor de idade')
    else:
        print(f'\nTemos \033[1;32m{contp}\033[m pessoas maiores de idade\n'
              f'E \033[1;31m{contm}\033[m pessoas menores de idade')

"""1 - Escrevi esse programa sozinho após ler o enunciado, gostei do resultado. Agora  vou ver a resolução do professor
e ver se tem algo a aprimorar, ou uma maneira maais fácil de fazer. 18/02/2022 12:51

2 - Meu código ficou quase igual o do professor, por isso não reescrevi, a diferença é que ele fez uma variáve de idade
e eu calculei no if. Meu código também tem tratamentos  de singular e plural, se todos sãao menos ou maiores e cores. 18/02/2022 13:52"""
