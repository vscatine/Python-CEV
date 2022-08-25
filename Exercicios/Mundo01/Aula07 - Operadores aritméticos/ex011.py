# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e quantiade
# de tinta necessária para pintá-la. Sabendo que cada litro de tinta pinta uma área de 2m².
'''lp = float(input('Largura da parede em metros? ex: 2.75 >> '))
ap = float(input('Altura da parede em metros? ex: 3.70 >> '))
m2 = lp * ap
t = m2 / 2
print(f'm²(LxA) da parede = {m2:.2f} m²')
print(f'Total de litros de tinta necessários para pintar a parede: {t:.2f} l')
print('*É considerado 1l de tinta para 2m²')'''

'''l = float(input('Largura em metros da parede: '))
a = float(input('Altura  em metros da parede: '))
print(f'Área total: {l*a:.2f} m²')
print(f'Quantidade de tinta necessaria para a área: {(l*a)*(0.5)} l')'''

print('Preencha a largura e altura da sua parede para verificarmos a quantidade de tinta necessária')
l = float(input('Largura em metros: '))
a = float(input('Altura em metros: '))
m = l*a
print(f'Sua parede possuí {m:.2f} m²')
print(f'Quantidade de tinda necessária: {m*0.5:.2f} l')
