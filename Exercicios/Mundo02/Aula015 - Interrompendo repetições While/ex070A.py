"""Crie um programa que leia o NOME e o preço de vários PRODUTOS. O programa deverá perguntar se o usuário vai continuar.
No final mostre:
A - Qual é o total gasto na compra.
B - Quantos produtos custam mais de R$1000.00
C - Qual é o nome do produto mais barato."""
print('=' * 40)
print(f'{" BARATO PRA CARAMBA ":^40}')
print('=' * 40)
tot = mil = cont = menor = 0
npb = ' '  # Nome do produto  barato
while True:
    np = str(input('Nome do produto: ')).capitalize()
    pp = float(input('Preço do produto: R$'))
    cont += 1
    tot += pp
    if pp > 1000:
        mil += 1
    if cont == 1:
        menor = pp
        npb = np
    else:
        if pp < menor:
            menor = pp
            npb = np
    eu = ' '
    while eu not in 'SN':
        eu = str(input('Inserir mais um item? [S/N] ')).strip().upper()[0]
    if eu == 'S':
        print('-' * 40)
    else:
        break
print('=' * 40)
print(f'Valor total R${tot:.2f}')
if mil == 0:
    print('Nenhum produto custou mais de R$1000.00')
elif mil == 1:
    print(f'{mil} produto custou mais de R$1000.00')
else:
    print(f'{mil} produtos custaram mais de R$1000.00')
print(f'O produto mais barato é {npb} e custou R${menor:.2f}')

# Escrevi esse código antes de ver a resolução do professor, deixei ele mais organizado após ver as resoluções
# anteriores, mas acabei parando no mesmo problema de antes, não consegui fazer o produto de menor valor aparecer no
# final. Comecei a ver a resolução e até o segundo tópico, meu código e o do professor estavamm iguais, depois que vi
# ele fazendo o menor valor, consegui entender e fazer sozinho. Como sempre, tratei o plural na mensagem final e
# gostei do resultao. 02/03/2022 13:20
