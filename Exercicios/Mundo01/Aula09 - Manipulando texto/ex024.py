'''Crie um programa que leia o nome de uma  cidade e diga se ela começa ou não com o nome "SANTO".'''
c = input('Nome da Cidade: ').strip()
u = c.upper()
s = u[:5] == 'SANTO'
print(s)

# Depois de ver a solução do professor(ex024A), tentei escrever de outra forma.
