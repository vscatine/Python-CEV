"""Crie um programa que simule o funcionamento de um caixa eletrônico. No ínicio, pergunte ao usuário
qual será o valor sacado (número inteiro) e o programa vai informar quantas cedulas de cada valor serão
entregues. OBS: Cosidere que o caixa possui cédulas de R$50, R$20, R$10 e R$1"""
print('=' * 35)
print(f'{" VITOR BANK ":^35}')
print('=' * 35)
print(f'{"Bem vindo ao Vitor Bank!":^35}')
print('-' * 35)
s = int(input('Valor do saque: R$'))  # Valor do saque
while s <= 0:
    print('\033[1;31mValor inválido!\033[m\nDigite um valor >= R$1.00')
    s = int(input('Valor do saque: R$'))  # Valor do saque
while s >= 1:
    c50 = s // 50  # Quantas notas de 50
    r50 = s % 50  # Resto das notas de 50
    if c50 > 0:
        print(f'{c50} Cedulas de R$50.00')
    if r50 == 0:
        break
    if r50 > 0:
        c20 = r50 // 20
        r20 = r50 % 20
        if c20 > 0:
            print(f'{c20} cédulas de R$20.00')
        if r20 == 0:
            break
    if r20 > 0:
        c10 = r20 // 10
        r10 = r20 % 10
        if c10 > 0:
            print(f'{c10} cédulas de R$10.00')
        if r10 == 0:
            break
    if r10 > 0:
        c1 = r10 // 1
        print(f'{c1} cédulas de R$1.00')
        break
print('Saque finalizado!')

# Escrevi esse programa lendo o enunciado do exercício e vendo o programa do professor funcionando, sem ver a
# resolução dele. Gostei do resultado, a única coisa que não entendi 100% é pq as variaveis não funcionam com elif,
# digo isso baseado num dos testes que fiz durante a escrita do programa, os elifs não constam nesse código no
# momento. Vou ver a resolução e ver se tem algo a melhorar. 02/03/2022 10:08
