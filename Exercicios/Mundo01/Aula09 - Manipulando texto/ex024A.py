'''Crie um programa que leia o nome de uma  cidade e diga se ela começa ou não com o nome "SANTO".'''
c = input('Nome da Cidade: ').strip()
print(c[:5].upper() == 'SANTO')
