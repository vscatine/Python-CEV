'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
para salários superiores a R$1250.00 calcule um aumento de 10% para os inferiores ou iguais. o aumento é de 15%'''
sa = float(input('Valor do salário atual: R$'))
if sa > 1250.00:
    ns = sa + (sa * 0.10)
    print(f'Valor do aumento 10%: R${sa * 0.10:.2f}')
else:
    ns = sa + (sa * 0.15)
    print(f'Valor do aumento  de 15%: R${sa * 0.15:.2f}')
print(f'Novo salário: R${ns:.2f}')
# Forma como eu escrevi após ver a resolução de exercício do professor.
# Mesclei a forma como eu havia escrito antes com a forma do professor. 10/02/2022
