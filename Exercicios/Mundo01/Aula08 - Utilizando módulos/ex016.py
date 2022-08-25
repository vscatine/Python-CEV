#Crie um programa que leia um número  real qualquer pelo teclado e mostre a sua porção inteira.
#EX: Digite 6.127 a parte inteira desse número é 6.

'''from math import trunc
n = float(input('Digite um valor: '))
print (f'O valor principal foi {n} e sua parte inteira  é {trunc(n)}')'''

n = float(input('Digite um valor:'))
print(f'O valor digitado foi {n} e sua parte inteira é {int(n)}')