'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da
casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
ou então o empréstimo será negado.'''
from time import sleep
print('Olá! Vamos simular seu financiamento e para isso preciso de algumas informações')
sleep(3)
financiamento = float(input('Qual o valor total do financiamento? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos financiar? '))
prestação = financiamento / (anos * 12)
limite = salario * 0.3
print(f'Para quitar um financiamento de R${financiamento:.2f} em {anos} anos')
print(f'a prestação será de R${prestação:.2f} mensais por {anos * 12} meses')
print()
print('O valor da prestação mensal nao pode exceder 30% do seu salário')
print('PROCESSANDO...')
sleep(3)
if  prestação > salario:
    print('\033[1;31mFINANCIAMENTO NEGADO\033[m')
else:
    print('\033[1;32mFINANCIAMENTO APROVADO!\033[m')
# Reescrevi após ver a resolução do professor, não mudei muita coisa, só deixei mais agradável. 14/02/2022 15:31