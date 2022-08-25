"""Crie uma TUPLA com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depois mostre:
A - Apenas os 5 primeiros colocados.
B - Os últimos 4 colocados.
C - Uma lista com os times em ordem alfabética.
D - Em que posição na tabela está o time da CHAPECOENSE."""
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense',
         'Atlético-MG',  'Botafogo', 'Athletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print(f'\033[1;33m{" CAMPEONATO BRASILEIRO 2018 ":=^40}\033[m')

print('\n\033[1;32mTabela\033[m')
for p5 in range(0, 20):
    print(f'{p5+1}º {times[p5]}')

print('\n\033[1;32mCinco Primeiros Colocados\033[m')
for p5 in range(0, 5):
    print(f'{p5+1}º {times[p5]}')
# Item A do exercício está funcionando, não sei se perfeitamente, pq fiz a "gambiarra" de somar 1 na posição.

print('\n\033[1;31mQuatro Últimos Colocados\033[m')
for u4 in range(-4, 0):
    print(f'{times[u4]}')
# Item B está funcionando parcialmente, não consegui fazer aparecer a posição que os times estão de forma correta.

print('\n\033[1;36mLista dos Times em ordem alfabética\033[m')
print(f'{sorted(times)}')
# Item C está funcionando parcialmente, não consegui fazer aparecer em lista, só um do lado do outro.

print('\n\033[1;35mChapecoense está na posição:\033[m')
print(f'{times.index("Chapecoense") + 1}º')
# Item D está funcionando, não sei se perfeitamente pq eu fiz aquela "gambiarra" de somar 1 para mostrar a posição
# correta do time, já que na tupla existe a posição 0 e na tabela do campeonato não.

# Considerações feitas nos itens do exercício durante o código. Fiz esse código apenas lendo o enunciado, depois vou
# ver a resolução do professor, para eu poder corrigir o que não consegui fazer. 03/03/2022 13:57 

# Acabei de ver a resoluão do professor, ele fez de uma forma muito mais "simples", porém, menos estética do que a
# minha, vou escrever a baixo o código como ele fez. Outr coisa, somar 1 para chegar na posição correta, que eu achei
# ser um gambiarra, também foi a soluçãao dele. 05/03/2022

print(f'\nPRÓXIMO PROGRAMA\n')
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense',
         'Atlético-MG',  'Botafogo', 'Athletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')
print(f'Lista dos times: {times}')
print('-=' * 40)
print(f'Cinco primeiros colocados: {times[0:5]}')
print('-=' * 40)
print(f'Últimos 4 colocados: {times[-4:]}')
print('-=' * 40)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 40)
print(f'Chapecoense está na {times.index("Chapecoense") + 1}ª posição')

# Vou procurar nos comentários para ver se alguém resolveu os dois problemas que eu não consegui no meu código.
# 05/03/2022 10:09
print('\nAJUSTANDO MEU PROGRAMA\n')
times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense',
         'Atlético-MG',  'Botafogo', 'Athletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
         'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print(f'\033[1;33m{" CAMPEONATO BRASILEIRO 2018 ":=^40}\033[m')

print('\n\033[1;32mTabela\033[m')
for p5 in range(0, 20):
    print(f'{p5+1}º {times[p5]}')

print('\n\033[1;32mCinco Primeiros Colocados\033[m')
for p5 in range(0, 5):
    print(f'{p5+1}º {times[p5]}')
# Item A do exercício está funcionando, não sei se perfeitamente, pq fiz a "gambiarra" de somar 1 na posição.

print('\n\033[1;31mQuatro Últimos Colocados\033[m')
for u4 in range(-4, 0):
    print(f'{times[u4]}')


print('\n\033[1;36mLista dos Times em ordem alfabética\033[m')
print(f'{sorted(times)}')
# Item C está funcionando parcialmente, não consegui fazer aparecer em lista, só um do lado do outro.

print('\n\033[1;35mChapecoense está na posição:\033[m')
print(f'{times.index("Chapecoense") + 1}º')

