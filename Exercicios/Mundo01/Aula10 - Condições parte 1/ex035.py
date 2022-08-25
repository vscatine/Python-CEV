'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
podem ou não formar um triângulo.'''
a = float(input('Comprimento da 1ª reta: '))
b = float(input('Comprimento da 2ª reta: '))
c = float(input('Comprimento da 3ª reta: '))
# Testando a primeira menor reta
m1 = a
if b < a and b < c:
    m1 = b
if c < a and c < b:
    m1 = c
# Testando a segunda menor reta
m2 < m1
print( m1, m2)
