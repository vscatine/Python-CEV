'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
podem ou não formar um triângulo.'''
print('-='*20)
print('ANALISADOR DE TRIÂNGULOS')
print('-='*20)
a = float(input('Comprimento da 1ª reta: '))
b = float(input('Comprimento da 2ª reta: '))
c = float(input('Comprimento da 3ª reta: '))
# A reta deve ser menor do que a soma do comprimento das outras duas retas
if a < b + c and b < a + c and c < a + b:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')
print('--- Deu certo, vou escrever a formula invertida a baixo---')

'''a = float(input('Comprimento da 1ª reta: '))
b = float(input('Comprimento da 2ª reta: '))
c = float(input('Comprimento da 3ª reta: '))
# A reta deve ser menor do que a soma do comprimento das outras duas retas
if a + b > c and b + c > a and c + a > b:
    print('Não é possível formar um triângulo')
else:
    print('Rolou')
# Não entendo pq o "inverso" da formula não dá certo. 11/02/2022'''