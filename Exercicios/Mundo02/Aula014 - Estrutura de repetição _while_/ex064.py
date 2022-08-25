"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""
c = -1
n1 = 0
while n1 != 999:
    n1 = int(input('Digite um número: '))
    n2 = n1
    soma = n1 + n2
    c += 1
print(f'{c} número lidos com soma igual a {soma}')
"""n1  n2
1 - 2 - 3 - 4 
    n1  n2"""

# Escrevi esse programa sem ver a resolução antes. Conseguifazer a contagem de números ficar correta, talvez com uma
# gambiarra, mas não consegui fazer a soma funcionar.
