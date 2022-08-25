"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO"""
n1 = float(input('Nota avaliação mensal: '))
n2 = float(input('Nota avaliação bimestral: '))
m = (n1 + n2) / 2
print(f'Tirando {n1:.1f} e {n2:.1f} a média do aluno(a) é {m:.1f}')
if m < 5:
    print(f'O(a) aluno(a) está \033[1;31mREPROVADO\033[m')
elif 5 <= m < 7:
    print('O(a) aluno(a) está de \033[1;33mRECUPERAÇÃO\033[m')
elif m >= 7:
    print('O(a) aluno(a) está \033[1;32mAPROVADO\033[m')
