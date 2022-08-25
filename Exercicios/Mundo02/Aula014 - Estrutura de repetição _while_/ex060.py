"""Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120"""
# Usando While e conta manual
n = int(input('Digite um número: '))
c = n  # Contador
f = 1  # Fatorial
while c > 0:
    print(c, end=' ')
    print('x ' if c > 1 else '= ', end='')
    f *= c
    c -= 1
print(f)

# Usando for e conta manual
n = int(input('Digite um número: '))
f = 1
for c in range(n, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f)

# usando módulo math.factorial
from math import factorial
n = int(input('Digite um número: '))
f = factorial(n)
print(f'{n}! = {f}')

# Usando while e módulo math.factorial
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = factorial(n)
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print(f)

# Usando for e módulo math.factorial
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print(f'{n}! = ', end='')
for c in range(n, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
print(f)

# Precisei ver a resolução do professor para fazer esse, mas consguir entender. Reescrevi o exercício de 5 formas
# diferentes, todas descritas no código. 22/02/2022 10:58 
