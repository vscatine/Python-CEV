"""Crie um programa que tenha uma tupla totalmente preenchida com uma contagem POR EXTENSO, de zero até vinte.
Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso"""

contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
            'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n = -1
while n < 0 or n > 20:
    n = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {contagem[n]}')

# Escrevi esse código apenas lendo o enunciado. Está funcionando corretamente. Depois eu vou ver a resolução do
# proofessor para ver se preciso aprimorar algo. 03/03/2022 13:15
print(f'\nPróximo programa\n')
cont2 = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
         'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            print(f'Você digitou o número {cont2[n]}')
            break
    r = ' '
    if r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r == 'N':
            break
print('Fim do programa. Volte sempre!')

# Vi a resolução do professor e nossos programas ficaram quase identicos, exceto, por ele ter usado o while True,
# que eu não tinha pensado quando escrevi. Também coloquei a opção do usuário continuar digitando novos números até
# pedir para o programa parar. # 05/03/2022 09:31
