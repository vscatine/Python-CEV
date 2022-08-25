"""Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos"""
pt = int(input('Qual o primeiro termo da PA? '))
qt = int(input('Quantos termos vamos calcular? '))
r = int(input('Qual a razão da PA? '))
c = 1  # contador
cd = 1  #contador dois
fim = False
while not fim:
    while c <= qt:
        print(pt, end='')
        print(' → ' if c < qt else ' → FIM', end='')
        pt += r
        c += 1
    eu = int(input('\nMais quantos termos dessa PA você quer ver? '))  # Escolha do usuário
    if eu < 0:
        print('Opção inválida!')
    elif eu == 0:
        fim = True
        print('Finalizando...')
    elif eu > 0:
        while cd <= eu:
            print(pt, end='')
            print(' → 'if cd < eu else ' → FIM',end='')
            pt += r
            cd +=1
print('Fim do programa. Volte Sempre!')

# Escrevi esse código sozinho, só lendo o enunciado. O programa funcionou +-, ele continua a PA depois que o usuário
# preenche a primeira vez, mas a partir da segunda ele não faz direito. Travei nesse ponto e vou ver a resolução do
# professor para  continuar. De qualquer forma, estou feliz de ter conseguido chegar em algum lugar. 23/02/2022
