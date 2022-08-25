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
print(f'Você nasceu em {an} e tem {i} anos.')
if i <= 9:
    print('Sua categoria é MIRIM')
elif 9 < i <= 14:
    print('Sua categoria é INFANTIL')
elif 14 < i <= 19:
    print('Sua categoria é JÚNIOR')
elif 19 < i <= 25:
    print('Sua categoria é SÊNIOR')
elif i > 25:
    print('Sua categoria é MASTER')
