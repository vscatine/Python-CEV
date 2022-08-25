"""Desenvolva um programma que leia o NOME, IDADE E SEXO de 4 pessoas. No final do programa, mostre:
- a média de idade do grupo
- Qual o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos"""
conti = 0  # Contador idades
contmv = 0  # contador mulher - 20 anos
ihv = 0  # ihv = idade homem mais velho
nhv = 0  # nhv = nome do homem mais velho
conth = 0  # contagem de homens
for p in range(1, 5):
    print(f'{f" {p}ª PESSOA ":-^30}')
    n = str(input('Nome: ')).strip().title()
    i = int(input('Idade: '))
    s = str(input('Sexo (M/F): ')).strip().upper()
    conti += i  # soma das idades
    mi = conti / p  # média das idades
    if p == 1 and s == 'M':
        ihv = i
        nhv = n
    if s == 'M' and i > ihv:
        ihv = i
        nhv = n
    if s == 'F' and i < 20:
        contmv += 1
    if s == 'M':
        conth += 1

print(f'\nA média de idade do grupo é {mi:.1f}')
if conth == 0:
    print('Não há nenhum homem nesse grupo.')
else:
    print(f'O homem mais velho do grupo tem {ihv} anos e se chama {nhv}')
if contmv == 0:
    print('Não há nenhuma mulher com menos de 20 anos nesse grupo.')
elif contmv == 1:
    print(f'{contmv} mulher nesse grupo tem menos de 20 anos')
else:
    print(f'{contmv} mulheres nesse grupo tem menos de 20 anos.')
