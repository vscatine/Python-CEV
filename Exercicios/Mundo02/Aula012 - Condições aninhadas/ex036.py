'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da
casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
ou então o empréstimo será negado.'''

finan = float(input('Qual o valor a ser financiado? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos você quer pagar o financiamento? '))
mes = anos * 12
limite = salario * 0.3
valpar = finan / mes
if valpar > limite:
    print(f'\033[31mFINANCIAMENTO NEGADO\033[m prestação mensal de R${valpar:.2f} excede 30% do salário R${limite:.2f}.')
else:
    print(f'\033[32mFINANCIAMENTO  APROVADO!\033[m você pagará {mes} prestações de R${valpar:.2f} por {anos} anos.')

# Forma como eu escrevi ante de ver a resolução do exercício pelo professor: 14/02/2022 15:01
