"""Crie um programa que tenha uma tupla única como nomes de produtos  e seus respectivos preços, na sequência. No
final, mostre uma listagem de preços, organizando os dados em forma tabular. """

"""tu = ('Hamburguer', 13.00, 'X-Burger', 15.00, 'X-Bacon', 18.00, 'X-Absurdo', 100.55, 'X-Salada', 18.00)
print(f'{" Burger Bom & Bacana ":=^35}')
print(f'{tu[0]:<10} {"":.^15} R${f"{tu[1]:.2f}":>4}')
print(f'{tu[2]:<10} {"":.^15} R${f"{tu[3]:.2f}":>4}')
print(f'{tu[4]:<10} {"":.^15} R${f"{tu[5]:.2f}":>4}')
print(f'{tu[6]:<10} {"":.^15} R${f"{tu[7]:.2f}":>4}')"""

# Bom, fiz esse código lendo o enunciado e vendo o programa do professor funcionando, sinto que fiz uma bela
# gambiarra, e o código não parece nenhum pouco prático, já que digitei linha por linha, mas foi a única forma que
# consegui pensar, para resolver esssa questão. Vou ver a resolução e ver como melhorar. 05/03/2022 09:05
tu = ('Hamburguer', 13.00,
      'X-Burger', 15.00,
      'X-Bacon', 18.00,
      'X-Absurdo', 100.55,
      'X-Salada', 18.00,)
print(f'{" Burger Bom & Bacana ":=^35}')
for pos in range(0, len(tu)):
    if pos % 2 == 0:
        print(f'{f"{tu[pos]} ":.<20}', end='')
    else:
        print(f' ${tu[pos]:>3.2f}')
