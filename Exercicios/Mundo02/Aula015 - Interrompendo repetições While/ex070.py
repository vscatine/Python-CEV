"""Crie um programa que leia o NOME e o preço de vários PRODUTOS. O programa deverá perguntar se o usuário vai continuar.
No final mostre:
A - Qual é o total gasto na compra.
B - Quantos produtos custam mais de R$1000.00
C - Qual é o nome do produto mais barato."""
tot = 0  # Total da soma dos valores dos produtos
cm = 0  # Contador de produtos com valor > R$ 1000.00

while True:
    dp = str(input('Descrição do produto: ')).strip().title()
    pp = float(input('Preço do produto: R$'))
    tot += pp
    mv = pp  # Menor valor
    npb = dp
    if pp > 1000:
        cm += 1
    eu = str(input('Inserir próximo produto? [S/N] ')).strip().upper()[0]
    while eu not in 'SN':
        print('\033[1;31mOpção inválida!\033[m Digite S para Sim e N para Não')
        eu = str(input('Inserir próximo produto? [S/N] ')).strip().upper()[0]
    if eu == 'S':
        print('-=' * 20)
        print('Inserindo...')
        if pp < mv:
            mv = pp
            npb = dp
    elif eu == 'N':
        break
print(f'Valor total: R${tot:.2f}\n'
      f'{cm} produtos custam mais de R$1000.00\n'
      f'{npb} é o produto mais barato e custa R${mv:.2f}')

# Escrevi esse código sozinho sem ver a resolução do professor. A única coisa que não consegui fazer funcionar foi o
# produto com menor valor, vou ver a resolução para descobrir onde eestou errando. 02/03/2022 09:10
