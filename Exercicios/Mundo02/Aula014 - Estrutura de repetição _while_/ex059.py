"""Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. """
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
om = 0  # Opção do menu
while om != 5:
    print('[ 1 ] Somar\n'
          '[ 2 ] Multiplicar\n'
          '[ 3 ] Qual o maior\n'
          '[ 4 ] Analisar novos números\n'
          '[ 5 ] Sair do programa')
    om = int(input('>>>>>> Qual é a sua opção? '))
    if om == 1:
        s = n1 + n2  # Soma
        print(f'{n1} + {n2} = {s}')
    elif om == 2:
        m = n1 * n2  # Multiplicação
        print(f'{n1} x {n2} = {m} ')
    elif om == 3:
        if n1 > n2:
            ma = n1
        else:
            ma = n2
        print(f'Entre {n1} e {n2} o maior valor é {ma}')
    elif om == 4:
        print('Informe os novos valores:')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif om == 5:
        print('Finalizando o programa...')
    else:
        print('Opção inválida!')
    print('-=' * 15)
print('Fim do programa. Volte sempre!')

# Precisei ver a resolução para sair do zero, não estava conseguindo iniciar o exercício sozinho.
# Gostei do resultado, mas, amanhã cedo vou melhorar esse programa. 21/02/2022 22:33
