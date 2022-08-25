"""Desenvolv um programa que leia o primeiro termo e a razão de um PA (Progressão aritmética).
no final, mostre os 10 primeiros termos dessa progressão."""
t = int(input('Qual o primeiro termo? '))
r = int(input('Qual a razão? '))
d = t + (10 - 1) * r  # Encontrando o décimo termo
for c in range(t, d + 1, r):
    print(c, end=' → ')
print('FIM')

# consegui escrever o código básico, sem a formula... vi a aula até ele dizer que precisava de uma formula,
# pesquisei  a formula e consegui  resolver o resto. 17/02/2022 12:02
