"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO"""
n1 = float(input('Nota avaliação mensal: '))
n2 = float(input('Nota avaliação bimestral: '))
m = (n1 + n2) / 2
if m < 5:
    print(f'Média \033[1;31m{m:.1f}\033[m abaixo de 5.0: \033[1;31mREPROVADO\033[m.')
elif m >= 5 or m < 7:
    print(f'Média \033[1;33m{m:.1f}\033[m entre 5.0 e 6.9: \033[1;33mRECUPERAÇÃO\033[m')
elif m >= 7:
    print(f'Média \033[1;32m{m:.1f}\033[m igual ou superior a 7.0: \033[1;32mAPROVADO\033[m')

# Escrevi antes de ver a resolução do exercício pelo  professor. 14/02/2022 17:35