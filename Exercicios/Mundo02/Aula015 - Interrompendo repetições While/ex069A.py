"""Crie um programa que leia a IDADE e o SEXO de várias pessoas. A cada pessoa cadastrada, o programa deverá
perguntar se o usuário quer ou não continuar. no final, mostre:
A - Quantas pessoas tem mais de 18 anos.
B - Quantos homens foram cadastrados
c - Quantas muheres tem menos de 20 anos"""
print('='*35)
print(f'{" CADASTRO DE PESSOAS ":^35}')
print('='*35)
cd = ch = cm = 0
# cd = Contador > 18 ch = Contador homens cm = contador mmulheres < 20
print('\033[32mInserindo primeiro registro... \033[m')
while True:
    i = int(input('Idade: '))
    s = ' '
    while s not in 'FM':
        s = str(input('Sexo [F/M]: ')).strip().upper()[0]
    if i > 18:
        cd += 1
    if s == 'M':
        ch += 1
    if s == 'F' and i < 20:
        cm += 1
    eu = ' '
    while eu not in 'SN':
        eu = str(input('Cadastrar próximo? [S/N] ')).strip().upper()[0]
    if eu == 'S':
        print('-' * 35)
        print('\033[33mInserindo novo registro...\033[m')
    else:
        break
print('-=' * 18)
print('\033[1;32mResulados:\033[m')
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

# Reescrevi após ver a solução do professor. Na verdade, nossos códigos ficaram muito parecidos, ele só fez os
# parâmetros numa parte diferente do que eu fiz, o que não afetou em nada a funcionalidade do programa. Usei
# também o que ele mostrou no exercício anterior, de colocar o parametro que o usuário vai preencher como vazio e
# tratar o while em baixo, vejo que o positivo de fazer isso é que o programa funcionando fica mais limpo e do jeito
# que eu fiz, mostrando uma mensagem de erro pro usuário, deixa o programa um pouco mais "feio". Vou começar a adotar
# esse metódo. 02/03/2022 12:26
