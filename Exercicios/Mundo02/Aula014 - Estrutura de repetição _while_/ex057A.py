"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
caso esteja errado, peça a digitação novamente até ter um valor correto."""
s = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while s not in 'FM':
    s = str(input('OPÇÃO INVÁLIDA! \nPor favor, digite seu sexo [M\F]: ')).strip().upper()[0]
print(f'Sexo \033[1;32m{s}\033[m registrado com sucesso!')
