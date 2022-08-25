"""Crie um programa que leia a IDADE e o SEXO de várias pessoas. A cada pessoa cadastrada, o programa deverá
perguntar se o usuário quer ou não continuar. no final, mostre:
A - Quantas pessoas tem mais de 18 anos.
B - Quantos homens foram cadastrados
c - Quantas muheres tem menos de 20 anos"""
cd = 0  # Contador maiores de 18 anos
ch = 0  # Contador de homens
cm = 0  # Contador de mulheres com menos de 20 anos
print('\033[32mInserindo primeiro registro... \033[m')
while True:
    i = int(input('Idade: '))
    s = str(input('Sexo [F/M]: ')).strip().upper()[0]
    while s not in 'FM':
        print('\033[1;31mOpção inválidada!\033[m\nDigite F para feminino e M para Masculino.')
        s = str(input('Sexo [F/M]: ')).strip().upper()[0]
    eu = str(input('Cadastrar próximo? [S/N] ')).strip().upper()[0]  # Escolha do usuário
    while eu not in 'SN':
        print('\033[1;31mOpção inválida!\033[m Digite S para Sim e N para não')
        eu = str(input('Cadastrar próximo? [S/N] ')).strip().upper()[0]
    if eu == 'S':
        print('\033[33mInserindo novo registro...\033[m')
        print('-=' * 27)
    if i > 18:
        cd += 1
    if s == 'M':
        ch += 1
    if s == 'F' and i < 20:
        cm += 1
    if eu == 'N':
        break
print('\033[1;32mResulados:\033[m')
print('-=' * 27)
if cd == 0:
    print('Não foi registrada nenhuma pessoa com mais de 18 anos')
elif cd == 1:
    print(f'{cd} pessoa registrada com mais de 18 anos')
else:
    print(f'{cd} pessoas registadas com mais de 18 anos.')
if ch == 0:
    print('Não foi registarado nenhum homem.')
elif ch == 1:
    print(f'{ch} homem registrado.')
else:
    print(f'{ch} homens registrados.')
if cm == 0:
    print('Não foi registrada nenhuma mulher com menos de 20 anos.')
elif cm == 1:
    print(f'{cm} mulher com menos de 20 anos registrada.')
else:
    print(f'{cm} mulheres com menos de vinte anos registradas.')

# Escrevi esse programa apenas lendo o enunciado. Gostei bastante do resultado e das tratativas que fiz. De qualquer
# forma, vou ver a resolução do professor e verificar se preciso alterar algo. 28/02/2022 15:58

