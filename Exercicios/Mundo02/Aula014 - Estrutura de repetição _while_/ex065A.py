"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""
r = 'S'
cont = soma = media = menor = maior = 0
while r == 'S':
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    cont += 1
    soma += n
    if cont == 1:
        menor = maior = n
    else:
        if n < menor:
            menor = n
        elif n > maior:
            maior = n
media = soma / cont
print(f'\nVocê digitou {cont} números\n'
      f'A soma entre eles é igual a {soma}\n'
      f'A média é {media:.2f}\n'
      f'O menor valor é {menor}\n'
      f'O maior valor é {maior}')
