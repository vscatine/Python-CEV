'''Crie um programa que leia o nome de uma pessoa e diga  se ela  tem "SILVA" no nome.'''
n = input('Nome Completo: ')
t = n.upper()
t1 = t.find('SILVA')
print(f'Possuí "SILVA"? {t1} ')
'''Teste que eu fiz antes de assistir a resolução do professor, está funcionando,
mas de uma forma meio precaria'''

n = input('Nome Completo: ').upper()
print(f'Seu nome tem Silva? {n.find("SILVA")}')

'''A Cima outra solução que eu escrevi, após assistir somente o início da resolução do professor.
o resultado foi o mesmo, porém escrito sem variáveis.'''

