'''Faço um programa que leia um ângulo qualquer e mostre na tela o valor de seno, coseno e tangente
 desse ângulo.'''
import math
a = float(input('Digite um ângulo qualquer: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print(f'Seno: {s:.2f}\nCosseno: {c:.2f}\nTangente: {t:.2f}')