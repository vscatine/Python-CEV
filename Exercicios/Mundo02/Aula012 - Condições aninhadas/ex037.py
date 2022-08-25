'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''
n = int(input('Digite um número qualquer: '))
print("""Escolha uma das bases para conversão: 
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL""")
o = int(input('Escolha sua opção: '))
if o == 1:
    print(f'{n} é {bin(n)[2:]} em BINÁRIO')
elif o == 2:
    print(f'{n} é {oct(n)[2:]} em OCTAL')
elif o == 3:
    print(f'{n} é {hex(n)[2:]} em HEXADECIMAL')
else:
    print('\033[1;31mOPÇÃO INVÁLIDA\033[m')
