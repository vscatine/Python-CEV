"""Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""
# Minha solução após ver a resolução do exercício 24/02/2002 11:00
n = 0
c = -1  # Contador
soma = 0
while n != 999:
    n = int(input('Digite um número: '))
    c += 1
    soma += n
print(f'Você digitou {c} números e a soma entre eles é igual a {soma - 999}')

print('\n\033[1;35mPROXIMO PROGRAMA\033[m\n')

# Solução do professor, sem subtrair 999 da soma e nem -1 do contador. 24/02/2022 11:09
c = 0
soma = 0
n = int(input('Digite um número: '))
while n != 999:
    c += 1
    soma += n
    n = int(input('Digite um número: '))
print(f'{c} números digitados e a soma entre eles é {soma}')
# Confesso que não entendi muito bem como funciona a solução apresentada a cima. 24/02/2022 11:35

print('\n\033[1;36mPRÓXIMO PROGRAMA\033[m\n')

# reescrevendo da primeira forma para praticar 24/02/2022 11:59
# resscrevi e sem querer acabei percebendo uma nova forma. Se eu colocar o input no fim do while, não preciso colocar 
# -999 na soma. Eu ainda não entendi muito bem o pq disso, igual na forma que o professor passou. 24/02/2022 12:31 
print(f'\033[1;32m{" SOMANDO QUANTOS NÚMEROS VOCÊ DIGITAR ":~^50}\033[m')
print(f'\033[31m{" digite 999 para finalizar ":^50}\033[m')
n = 0
c = -1
soma = 0
while n != 999:
    c += 1
    soma += n
    n = int(input('Digite um número: '))
if c == 0:
    print('\033[1;31mNENHUM NÚMERO DIGITADO!\033[m')
elif c == 1:
    print('\033[1;33mApenas UM número digitado!\033[m\n'
          '\033[1mDigite mais de um número para ver a soma no final!\033[m')
else:
    print(f'\nVocê digitou \033[1;36m{c}\033[m números e a soma entre eles é igual a \033[1;32m{soma}\033[m')
print('\033[1;36m\nPRÓXIMO PROGRAMA\033[m\n')

# Reescrevendo da forma que o professor explicou. Apenas para praticar. 24/02/2022 12:35
print(f'\033[1;34m{" SOMANDO OS NÚMEROS DIGITADOS ":=^50}\033[m')
print(f'\033[33m{"digite 999 para  finalizar":^50}\033[m')
c = 0
soma = 0
n = int(input('Digite um número: '))
while n != 999:
    c += 1
    soma += n
    n = int(input('Digite um número: '))
if c == 0:
    print('\033[1;31mNENHUM NÚMERO DIGITADO!\033[m')
elif c == 1:
    print('\033[1;33mApenas UM número digitado!\033[m\n'
          '\033[1mDigite mais de um número para ver a soma no final.\033[m')
else:
    print(f'\nForam digitados \033[1;33m{c}\033[m números e a soma entre eles é igual a \033[1;32m{soma}\033[m')
# Reescrevi da forma  do professor, mas ainda nao entendi 100% a solução. 24/02/2022 12:53
