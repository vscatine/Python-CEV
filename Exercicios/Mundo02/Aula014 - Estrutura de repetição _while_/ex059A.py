"""Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso. """
fim = False
while not fim:  # fim == False: # ambas as opções tem o mesmo efeito
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o seguno valor: '))
    eu = int(input('Selecione o que quer fazer:\n'  # eu = Escolha do usuário
                   '[ 1 ] Somar\n'
                   '[ 2 ] Subtrair\n'
                   '[ 3 ] Multiplicar\n'
                   '[ 4 ] Mostrar qual é o  maior\n'
                   '[ 5 ] Inserir novos números\n'
                   '[ 6  ] Sair do programa\n'
                   '>>>>>> Qual é sua opção? '))
    if eu == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}\n')
    elif eu == 2:
        print(f'{n1} - {n2} = {n1 - n2}\n')
    elif eu == 3:
        mult = n1 * n2
        print(f'{n1} x {n2} = {mult}\n')
    elif eu == 4:
        if n1 > n2:
            maior = n1
            print(f'O maior valor é {maior}\n')
        elif n2 > n1:
            maior = n2
            print(f'O maior valor é {maior}\n')
        elif n1 == n2:
            print('Os valores são iguais\n')
    elif eu == 5:
        print('Claro! vamos lá...\n')
    elif eu == 6:
        fim = True
        print('Finalizando o programa...\n')
    else:
        print('OPÇÃO INVÁLIDA!\n')
print('Fim do programa. Volte sempre!')

# Reescrevi o código mudando pouquissímas coisas, resolvi não fazer com cores e etc para não perder tempo. 22/02/2022 09:47