"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles
(DESCONSIDERANDO O FLAG). """
print('Somando quantos números você digitar\n'
      'digite 999 para parar o programa\n')
soma = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} números e a soma entre eles é igual a {soma}')

# Escrevi esse programa sozinho antes de ver a resolução do professor. 28/02/2022 09:51
