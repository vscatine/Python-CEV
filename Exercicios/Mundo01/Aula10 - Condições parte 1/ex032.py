'''Faça um programa que leia um ano e diga se o mesmo e BISSEXTO.'''
import datetime
a = int(input('Que ano vamos analisar?\nColoque 0 para verificar o ano atual: '))
if a == 0:
    a = datetime.date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'O ano {a} é BISSEXTO')
else:
    print(f'O ano {a} NÃO é BISSEXTO.')

# 10/02/2022 - estudar mais %(resto de divisão), eu aina não entendo muito bem.