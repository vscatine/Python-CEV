'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
para salários superiores a R$1250.00 calcule um aumento de 10% para os inferiores ou iguais. o aumento é de 15%'''
sa = float(input('Valor do salário atual: R$'))
if sa > 1250.00:
    print(f'Aumento de 10%: R${sa*0.10:.2f}')
    print(f'Novo salário: R${sa+(sa*0.10):.2f}')
else:
    print(f'Aumento de 15%: R${sa*0.15:.2f}')
    print(f'Novo salário: R${sa+(sa*0.15):.2f}')
print('ESCRITO DE OUTRO FORMA:')
sa = float(input('Valor do salário atual: R$'))
if sa > 1250.00:
    print(f'Valor do aumento de 10%: R${(10*sa)/100:.2f}')
    print(f'Valor do novo salário: R${sa+((10*sa)/100):.2f}')
else:
    print(f'Valor do aumento de 15%: R${(15*sa)/100:.2f}')
    print(f'Valor do novo salário: R${sa+(15*sa)/100:.2f}')
#Essa foi a forma que eu escrevi antes de ver a resolução do professor. 10/02/2022
