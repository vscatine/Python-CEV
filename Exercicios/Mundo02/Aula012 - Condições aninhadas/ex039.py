'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
import datetime
a = int(input('Qual ano você nasceu? '))
c = datetime.date.today().year
if c - a < 18:
    print(f'Você tem {c - a} anos e não precisa se alistar ainda. '
          f'Você deverá se alsitar em {a + 18}')
elif c - a == 18:
    print(f'Você tem {c - a} anos e seu alistamento deve ser feito esse ano. ')
else:
    t = int(input("""Ja realizou seu alistamento militar? 
    Digite: [ 1 ] para SIM
            [ 2 ] para NÃO """))
    if t == 1:
        print(f'Perfeito! Seu alistamento deve ter sido em {a + 18}')
    elif t == 2:
        print(f'Você deveria ter se alistaddo em {a + 18}')
    else:
        print('OPÇÃO INVÁLIDA. tente  novamente.')
# Escrevi antes de ver a resolução do exercício pelo professor. 14/02/2022 16:42
