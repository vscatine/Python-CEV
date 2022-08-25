"""Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8"""
"""print(f'\033[1;33m{" SEQUÊNCIA DE FIBONACCI ":=^50}\033[m')
n = int(input('Quantos números da sequência você quer ver? '))
t1 = 0  # 1º termo
t2 = 1  # 2º termo
t3 = t1 + t2
c = 3  # Contador
print(f'{t1} - {t2} - ', end='')
while c <= n:
    print(t3, end='')
    print(' - ', end='')
    c += 1
    t1 = t2
    t2 = t3
    t3 = t1 + t2
print('FIM')"""
#  A baixo um exemplo visual da lógica, a primeira linha é que era,
#  a segunda a propria sequência de fibonacci
#  e a terceira os novos valores.
# t1  t2  t3
#  0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 - 21 - 34 - 55
#      t1  t2  t3
print(f'\033[1;36m{" SEQUÊNCIA DE FIBONACCI ":~^40}\033[m')
n = int(input('Quantos números da sequência você quer ver? '))
t1 = 0
t2 = 1
t3 = t1 + t2
c = 3  # Contador
t = 0  # Totalizador
print(f'{t1} - {t2} - ', end='')
while n != 0:
    t = t + n
    while c <= t:
        print(t3, end='')
        print(' - ', end='')
        c += 1
        t1 = t2
        t2 = t3
        t3 = t1 + t2

    print('PAUSA')
    n = int(input('Quantos números a mais da sequência você quer ver? '))
print(f'Sequência de fibonacci finalizada com {t} números mostrados.')

# Finalizei esse exercício ontem a noite, reescrevi da forma comum e fiz mais um perguntando quantos números a mais o
# usuário quer ver, igual o da fatoração. Olhei nos comentários do vídeo algumas outras soluções, mas a do professor
# foi a que fez mais sentido pra mim. 24/02/2022 08:55
