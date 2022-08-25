#Desenvolva um programa que leia as duas notas de um aluno. Calcule e mostre a sua média.
'''a = input('Nome do aluno:')
n1 = float(input('Nota mensal'))
n2 = float(input('Nota Bimestral'))
m = (n1+n2)/2
print(f'O aluno(a) {a} tirou {n1} na prova mensal e {n2} na bimestral\nFicando com a média {m} no bimestre.')'''
import math
n1 = float(input('Nota mensal: '))
n2 = float(input('Nota Bimestral'))
n3 = float(input('Avaliação continua'))
m = math.ceil((((n1+n2)/2) + n3) / 2)
print(f'Média final = {m:.2f}')
