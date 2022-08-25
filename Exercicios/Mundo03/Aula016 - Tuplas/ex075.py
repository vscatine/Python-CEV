"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A — Quantas vezes o valor 9 foi digitado.
B — Em que posição foi digitado o primeiro valor 3.
C — Quais foram os números pares."""
"""n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
tu = (n1, n2, n3, n4)

print(f'Você digitou os números: ', end='')
for n in tu:
    print(f'{n}', end=' ')

if tu.count(9) == 0:
    print('\nO número 9 não foi digitado nenhuma vez.')
else:
    print(f'\nO número 9 foi digitado {tu.count(9)} vezes')
if 3 not in tu[0:]:
    print('O número 3 não foi digitado nenhuma vez.')
else:
    print(f'O número 3 apareceu pela primeira vez na {tu.index(3) + 1}ª posição.')"""

# Eu consegui escrever esse código até o item B, acredito que está fucionando normalmente, como ainda não vi nenhua
# resolução, pq só estou vendo os exercícios na aula, não sei se somar 1 na posiçã é uma gambiarra ou não.
# Não estou conseguindo sair do lugar na questão dos números pares, vou retomar amanhã cedo. 03/03/2022 20:13
"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A — Quantas vezes o valor 9 foi digitado.
B — Em que posição foi digitado o primeiro valor 3.
C — Quais foram os números pares."""

n = tuple(int(input('Digite um número: '))for c in range(0, 4))
cp = 0  # Contador de números pares
if 9 in n:
    print(f'O número 9 foi digitado {n.count(9)} vezes.')
else:
    print('O número 9 não foi digitado nenhuma vez.')
if 3 in n:
    print(f'O número 3 apareceu na {n.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado nenhuma vez.')
for p in n:
    if p % 2 == 0:
        cp += 1
if cp == 0:
    print('Nenhum número par for digitado')
elif cp == 1:
    print('O número par digitado foi: ', end='')
    for p in n:
        if p % 2 == 0:
            print(p)
else:
    print('Os números pares digitados foram: ', end='')
    for p in n:
        if p % 2 == 0:
            print(p, end=' ')

# Meu programa tinha ficado ok, tirando a parte que eu não consegui fazer os números pares, mas eu também não usei a
# tuplu muito bem. Agora  que eu vi a resolução do professor, consegui entender direito como fazer, ainda olhei nos
# comentários e descobri outra forma de colocar as variáveis em uma tupla com uma única linha usando o for x in
# range(x, y), o professor copiou o input 4 vezes dentro do parenteses. 07/03/2022 10:28
