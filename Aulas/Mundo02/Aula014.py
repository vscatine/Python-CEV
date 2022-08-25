# Estrutura de repetição WHILE
# 1 exemplo
"""for c in range(1, 10):
    print(c)
print('FIM\n'
      '\033[1;31mVamos ver com o while?\033[m\n')

c = 1
while c < 10:
    print(c)
    c += 1
print('ACABOU')"""

# 2 exemplo
"""for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('FIM\n'
      '\033[1;33mAgora com o while!\033[m\n')
n = 1
while n != 0:
    n = int(input(f'Digite um valor: '))
print('Vamos ver se funfou')"""

# 3 exemplo
"""r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? (S/N): ')).upper().strip()
print('FIM')"""

# 4 exemplo
n = 1  # número
cp = 0  # contador de números pares
ci = 0  # contador de números ímpares
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 ==0:
            cp += 1
        else:
            ci += 1
print(f'Você digitou {cp} números  pares e {ci} números ímpares.')
print('FIM DO PROGRAMA')

