"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER"""
from datetime import date
an = int(input('Em que ano você nasceu? '))
i = date.today().year - an
print(f'O(A) atleta tem {i} anos e sua categoria é:')
if i <= 9:
    print('MIRIM')
elif i <= 14:
    print('INFANTIL')
elif i <= 19:
    print('JÚNIOR')
elif i <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
"""elif i > 25:
    print('MASTER')"""
