# Laços de repetição (parte 3)
soma = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou {cont} números e a soma entre eles é igual a {soma}')
