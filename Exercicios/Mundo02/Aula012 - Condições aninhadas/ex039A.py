"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""
from datetime import date
n = int(input('Qual ano você nasceu? '))
a = date.today().year
i = a - n
if i < 18:
    print(f'Você completa {i} anos em {a}.')
    print(f'Ainda faltam {18 - i} anos para seu alistamento.')
    print(f'Seu alistamento será em {n + 18}.')
elif i == 18:
    print(f'Esse ano você completa 18 anos.')
    print('Seu alistamento deve ser feito IMEDIATAMENTE!')
elif i > 18:
    t = int(input('Você já fez seu alistamento militar?\n'
                  'Digite : [ 1 ] para SIM\n'
                  '         [ 2 ] para NÃO\n'
                  'Resposta: '))
    if t == 1:
        print(f'Perfeito! Você deve ter se alsitado em {n + 18}.')
    elif t == 2:
        print(f'Você deveria ter se alsistado em {n + 18}.')
    else:
        print('OPÇÃO INVÁLIDA. Tente novamente.')
# Reescrevi usando variáveis parecidas com o professor, mas ainda gostei mais da minha soluão. 14/02/2022 17:07
