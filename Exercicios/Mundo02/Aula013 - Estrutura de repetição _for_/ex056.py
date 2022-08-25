"""Desenvolva um programma que leia o NOME, IDADE E SEXO de 4 pessoas. No final do programa, mostre:
- a média de idade do grupo
- Qual o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos"""
conti = 0  # soma das idades
contmv = 0  # contador de mulher  com menos de 20 anos
for p in range(1, 5):
    print(f'{f" {p}ª PESSOA ":-^30}' )
    n = str(input(f'Nome: ')).strip().title()
    i = int(input('Idade: '))
    s = str(input('Sexo (M/F): ')).strip().upper()
    conti += i
    mi = conti / p  # média de idade
    """if s == 'M':
        mv = i
        hv = n
        if i > mv:
            mv = i
            hv = n"""
    if s == 'F' and i < 20:
        contmv += 1
print(f'\nA média de idade desse grupo é: {mi:.1f}')
if contmv == 0:
    print('Não existe nenhuma mulher com menos de 20 anos nesse grupo.')
elif contmv == 1:
    print(f'Nesse grupo {contmv} mulher tem menos de 20 anos.')
else:
    print(f'Nesse grupo {contmv} mulheres tem menos de 20 anos')
# print(f'O homem mais velho é o {hv} e ele tem {mv} anos')

# fiz o código antes de de ver a resolução, consegui resolver a média de idade do grupo.
# tentei resolver o homem mais velho e não consegui fazer dar certo.
# não consegui pensar em  nada para resolver o das mulheres com menos de 20 anos.
# Vou ver a resolução do professor, ver se a minha média está ok ou preciso reescrver e vou descobrir como fazer os outros dois. 18/02/2022 15:18
# 15:30 - Vi o professor rodando o programa dele no ccomeço do vídeo e percebi como fazer as mulheres de 20 funcionar, agora só falta o homem mais velho.
