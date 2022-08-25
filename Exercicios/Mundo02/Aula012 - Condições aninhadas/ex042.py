"""Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será
formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes"""
# A reta deve ser menor do que a soma do comprimento das outras duas retas
r1 = float(input('1º segmento do triângulo: '))
r2 = float(input('2º segmento do triângulo: '))
r3 = float(input('3º segmento do triângulo: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triângulo!')
#if r1 == r2 and r1 == r3 and r2 == r1 and r2 == r3 and r3 == r1 and r3 == r2:
    if r1 == r2 == r3:
    print('O tipo do triângulo é EQUILÁTERO!')
    elif r1 == r2 != r3 or r1 == r3 != r2:
    print('o tipo do triângulo é ISÓSCELES')
else:
    print('Não é possível formar um triângulo')
