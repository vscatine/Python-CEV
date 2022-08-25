"""Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while"""
# tentei escrever essa sem ver o vídeo antes, basicamente não saí do lugar.
"""t = int(input('Qual o termo? '))
r = int(input('Qual a razão? '))
q = int(input('Quanto termos vamos calcular? '))
n = t + (q - 1) * r
c = q
while c <= q:
    c -= 1
    print(c)"""

# Solução do professor com pequenas mudanças
"""pt = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
c = 1
while c <= 10:
    print(f'{pt}',end='')
    print(' → ' if c < 10 else '', end='')
    pt += r
    c += 1"""

# Minha solução, permitindo que o ussuário diga quantos termos quer calcular
"""pt = int(input('Primeiro termo da PA: '))
qt = int(input('Quantos termos vamos calcular? '))
r = int(input('Razão da PA: '))
c = 1  # Contador para limitar os termos da PA, baseado na qtd de termos que o usuário determinar
while c <= qt:
    print(pt, end='')
    print(' → ' if c < qt else ' → FIM', end='')
    c += 1
    pt += r"""

# Reescrevi para praticar e ter certeza que entendi
pt = int(input('Primeiro termo da PA: '))
qt = int(input('Quantidade de termos da PA: '))
r = int(input('Razão da PA: '))
c = 1  # Contador de termos da PA
while c <= qt:
    print(pt, end='')
    print(' → ' if c < qt else ' → FIM', end='')
    pt += r
    c += 1
