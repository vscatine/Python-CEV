'''Crie um programa que leia 3 números e diga qual é o valor mais alto e qual o mais baixo. '''
a = int(input('1º valor: '))
b = int(input('2º valor: '))
c = int(input('3º valor:'))
#Testando o menor
me = a
if b<a and b<c:
    me = b
if c<a and c<b:
    me=c
#testando o maior
ma = a
if b>a and b>c:
    ma = b
if c>a and c>b:
    ma = c
print(f'O menor valor é {me}')
print(f'O maior valor é {ma}')
