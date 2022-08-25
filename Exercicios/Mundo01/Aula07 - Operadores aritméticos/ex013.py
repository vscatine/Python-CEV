#Faça um algoritmo que leia o salário de uma funcionário e mostre seu novo salário com 15%  de aumento.
s = float(input('Salário atual: R$'))
a = float(input('Percentual(%) de aumento: '))
sa = s + (s * a/100)
print(f'Valor do aumento: R${s*a/100:.2f}\nSalário com aumento: R${sa:.2f}')