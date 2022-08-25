"""Faça um programa que calcule a soma entre todos os números impares que são
multiplos de três e que se encontram no intervalo de 1 até 500"""
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c  # isso é a mesma coisa que soma = soma + c
        cont += 1  # isso é a mesma coisa que cont = cont + 1
print(f'A soma dos {cont} valores solicitados é {soma}')

'''Considerações: Aprendi mais uma vez a achar os ímpares utilizandoo próprio rang, sem um "if",
 isso deixa o processo mais leve pra o computador. e reescrevi o código usando as formulas que o professor passou.
 16/02/2022 14:53'''