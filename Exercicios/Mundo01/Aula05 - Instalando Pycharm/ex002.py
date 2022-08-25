'''Crie um programa que peça para escrever seu nome e de uma mensagem de boas vindos utilizando o nome.'''

n = input('Olá! Qual o  seu nome? ')
print('É um prazer te conhecer, \033[1;35m{}\033[m!' .format(n))
