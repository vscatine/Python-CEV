""" Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lido."""

for p in range(1, 6):
    kg = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = kg
        menor = kg
    else:
        if kg > maior:
            maior = kg
        if kg < menor:
            menor = kg
print(f'\nO maior peso lido foi {maior}\n'
      f'O menor peso lido foi {menor}')
# precisei ver a resolução do professor para entender esse. Ainda é um pouco confuso, mas analisando
# linha por linha consegui entender. 18/02/2002 14:12
