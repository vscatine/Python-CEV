'''Um professor quer sortear um de seus quatro  alunos a apagar o quadro. Faça um programa que ajude ele.
Lendo o nome deles e escreevendo o nome do escolhido.'''
import random
a1 = input('Nome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceiro aluno: ')
a4 = input('Nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
s = random.choice(lista)
print(f'O(A) aluno(a) sorteado(a) foi: {s}')