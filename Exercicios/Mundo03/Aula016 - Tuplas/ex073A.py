"""Crie uma TUPLA com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação.
Depois mostre:
A - Apenas os 5 primeiros colocados.
B - Os últimos 4 colocados.
C - Uma lista com os times em ordem alfabética.
D - Em que posição na tabela está o time da CHAPECOENSE."""
"""times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense',
         'Atlético-MG',  'Botafogo', 'Athletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print(f'\033[1;33m{" CAMPEONATO BRASILEIRO 2018 ":=^40}\033[m')

print('\n\033[1;32mTabela\033[m')
for t in range(0, 20):
    print(f'{t+1}º {times[t]}')

print('\n\033[1;32mCinco Primeiros Colocados\033[m')
for p5 in range(0, 5):
    print(f'{p5+1}º {times[p5]}')

print('\n\033[1;31mQuatro Últimos Colocados\033[m')
for u4 in times[-4:]:
    print(f'{times.index(u4)}º', u4)

print('\n\033[1;36mLista dos Times em ordem alfabética\033[m')
for alf in sorted(times):
    print(alf)

print('\n\033[1;35mChapecoense está na posição:\033[m')
print(f'{times.index("Chapecoense") + 1}º Posição')

# Achei um comentário que deu certo o que eu queria resolver, aparecer a posição dos útimos colocados e mostrar a
# lista com os times em ordem alfabética, um em cima do outro. Eu vou reescrever esse código inteiro para fixar essa
# maneira de fazer. 05/03/2021 10:41

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense',
         'Atlético-MG',  'Botafogo', 'Athletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('Brasileirão 2018')
for lista in times:
    print(f'{times.index(lista) + 1}º', lista)
print('\nCinco primeiros colocados:')
for p5 in times[:5]:
    print(f'{times.index(p5) + 1}º', p5)
print('\nQuatro últimos colocados:')
for u4 in times[-4:]:
    print(f'{times.index(u4) + 1}º', u4)
print('\nLista dos times em ordem alfabética:')
for alfa in sorted(times):
    print(alfa)
print(f'\nChapecoense está na {times.index("Chapecoense") + 1}ª posição')"""

"""Crie uma TUPLA com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação.
Depois mostre:
A - Apenas os 5 primeiros colocados.
B - Os últimos 4 colocados.
C - Uma lista com os times em ordem alfabética.
D - Em que posição na tabela está o time da CHAPECOENSE."""
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense',
         'Atlético-MG',  'Botafogo', 'Athletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print('Campeonato Brasileiro 2018')
for t in times:
    print(f'{times.index(t) + 1}º', t)

print('\nCinco primeiros colocados')
for p5 in times[:5]:
    print(f'{times.index(p5) + 1}º', p5)

print('\nQuatro últimos colocados')
for u4 in times[-4:]:
    print(f'{times.index(u4) + 1}º', u4)

print('\nTimes em ordem alfabética')
for alf in sorted(times):
    print(alf)

print(f'\nChapecoense está na {times.index("Chapecoense") + 1}ª posição')
