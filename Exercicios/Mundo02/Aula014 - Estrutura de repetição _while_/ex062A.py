"""Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos"""
"""pt = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
qt = int(input('Quantidade de termos da PA: '))
c = 1  # Contador de termos da PA
total = 0
while qt != 0:
    total = total + qt
    while c <= total:
        print(pt, end='')
        print(' → ', end='')
        pt += r
        c += 1
    print('PAUSA')
    qt = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')
print('\nAÍ EM CIMA EU ESCREVI ACOMPANHANDO O VÍDEO, MESCLEI MEU CÓDIGO COM O DO PROFº\n'
      'AGORA VOU REESCREVER A BAIXO\n')"""
print(f'{" PROGRESSÃO ARITMÉTICA ":=^40}')
pt = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))
qt = int(input('Quantidade de termos da PA: '))
c = 1  # Contador
t = 0  # Total
while qt != 0:
    t += qt
    while c <= t:
        print(pt, end='')
        print(' → ', end='')
        pt += r
        c += 1
    print('PAUSA')
    qt = int(input('Quantos termos quer mostrar a mais? '))
print(f'Progressão finalizada com {t} termos mostrados.')

# Deixei um "comentário" no meio do programa, mas  vou descrever aqui do mesmo jeito. consegui fazer esse exercício
# após ver o vídeo de resolução do professor. Achei uma das variáveis dele redundante e tentei fazer do meu jeito,
# deu certo. A variavel em questão é quantidade de termos. O professor faz o programa começar com 10 e precisa criar
# outra variável, eu já deixo o usuário escolher quantos quer no ínicio. 23/02/2022 14:34
