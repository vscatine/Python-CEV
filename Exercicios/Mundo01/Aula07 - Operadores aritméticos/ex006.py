# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e riz quadrada

'''n1=int(input('Coloque um número aqui:'))
print(f'O dobro de {n1} é {n1*2}\nOtriplo de {n1} é {n1*3}\nA raiz quadrada de {n1} é {n1**(1/2):.3f}')'''
lc = {'cl': '\033[m',
      'g': '\033[1;32m',
      'y': '\033[1;33m',
       'r': '\033[1;31m',
       'bo': '\033[1m'}
n = float(input('Insira um nº aqui: '))
print(f'O dobro de{lc["y"]} {n} {lc["cl"]}é {lc["bo"]}{n*2}{lc["cl"]}')
print(f'O triplo de{lc["y"]} {n} {lc["cl"]}é {lc["bo"]}{n*3}{lc["cl"]}')
print(f'A raiz quadrada de{lc["y"]} {n} {lc["cl"]}é {lc["bo"]}{n**(0.5)}{lc["cl"]}')