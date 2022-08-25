"""Faça um programa que mostre a TABUADA de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo."""
while True:
    n = int(input('Quer a tabuada de qual número? '))
    print('-=' * 16)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n:2} x {c:2} = {n * c:3}')
    print('-=' * 16)
print('Fim do programa. Volte sempre!')

# Escrevi esse programa antes de ver a resolução do professor, só vi o programa dele rodando, que ele mostrou ainda
# durante a aula. 28/02/2022 10:01
