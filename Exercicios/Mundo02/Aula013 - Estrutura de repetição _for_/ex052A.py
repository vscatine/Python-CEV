"""faça um programa ue leia um número inteiro e diga sse ele é ou não um número primo """
print(f'{" ANALISADOR DE NÚMEROS PRIMOS ":=^40}')
n = int(input('Digite um número: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        cont += 1
        print('\033[32m', end='')
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
if cont == 1:
    print('\n\033[m1 só é divisível por ele mesmo')
else:
    print(f'\n\033[m{n} é divisível por {cont} numeros')
if cont == 2:
    print('Por isso \033[32mÉ UM NÚMERO PRIMO\033[m')
else:
    print('Por isso \033[31mNÃO É\033[m um número primo')

# reescrevi o programa usando cores e tratando singular e plural, no caso do número 1. 17/02/2022 13:38

