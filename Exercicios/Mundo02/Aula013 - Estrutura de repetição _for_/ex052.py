"""faça um programa ue leia um número inteiro e diga sse ele é ou não um número primo """
n = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        cont += 1
if cont == 1:
    print(f'{n} foi divisível {cont} vez')
else:
    print(f'{n} foi divisível {cont} vezes')
if cont == 2:
    print(f'{n} é um número primo.')
else:
    print(f'{n} não é um número primo')

# Escrevi esse código após ver a resolução do professor, pq não estava cosneguindo sozinho.
#  vou reescrever usando as cores como ele fez. 17/02/2022 13:00
