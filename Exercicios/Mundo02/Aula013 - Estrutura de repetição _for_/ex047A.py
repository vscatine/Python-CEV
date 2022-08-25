"""Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50"""
for c in range(1, 51):
    print('.', end='')
    if c % 2 == 0:
        print(c, end=' ')

print('\nA baixo temos uma forma com mesmo resultado, porém usando menos laços')

for c1 in range(2, 51, 2):
    print('.', end='')
    print(c1, end=' ')

# considerações: a primeira forma ficou basicamente igual a que eu havia escrito antes, mas eu tinha uma redundancia
# a segunda forma faz metade dos laços, tornando o pprocesso mais "leve" e tendo o mesmo resultado
# podemos verificar isso analisando os pontos de teste colocados em um print antes dos números pares.
