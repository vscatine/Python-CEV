"""Crie um programa que tenha uma tupla com várias palavras (Não usar acentos). Depois disso, você deve mostrar para
cada palavra, quais são os suas vogais. """
palavra = ('palavra', 'basquete', 'bola', 'comida', 'nigeria', 'osasco',
           'aleatoriedade', 'canivete', 'abacaxi', 'lynyrd skynyrd')
cv = 0  # Contador de vogais
for p in palavra:
    for letra in p:
        if letra.lower() in 'aeiou':
            cv += 1
    print(f'\nNa palavra {p.upper()} temos as vogais ', end='')
    print(f'{cv}')
