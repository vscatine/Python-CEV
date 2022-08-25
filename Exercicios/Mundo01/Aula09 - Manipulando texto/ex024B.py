'''Crie um programa que leia o nome de uma  cidade e diga se ela começa ou não com o nome "SANTO".'''
c = input('Qual a sua Cidade? ').strip().upper()
print(f'Sua cidade começa com "Santo"? {c[:5] == "SANTO"}')
