'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
se o valor ffor impar desconsidere-o.'''
soma = 0
cont = 0
for c in range(1,7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Você digitou {cont} valores PARES e a soma entre eles é {soma}')
