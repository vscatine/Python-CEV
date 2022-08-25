'''O mesmo professor do desafio anterior quer sortar a ordem da apresentação de trabalhos dos alunos.
 Faça  um programa que leia o nome dos quarto  alunos e mostre  a ordem sorteada.'''
import random
a1 = input('1º aluno(a): ')
a2 = input('2º aluno(a): ')
a3 = input('3º aluno(a): ')
a4 = input('4º aluno(a): ')
l = [a1, a2, a3, a4]
random.shuffle(l)
print(f'A ordem de apresentasão será:\n{l}')