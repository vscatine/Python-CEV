# Escreva um programa que leia um valor em metros e o exiba convertido em cm e mm.
'''m = float(input('Valor em metros(m)'))
km = m/1000
hm = m/100
dam= m/10
dm = m*10
c = int(m*100)
mm = int(m*1000)
print(f'{m} m = {km} km\n{m} m = {hm} hm\n{m} m = {dam} dam\n{m} m = {dm} dm\n{m} m = {c} cm\n{m} m = {mm} mm')'''

m = float(input('Valor em metro(m): '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
c = m*100
mm = m*1000

print(f'km = {km} km')
print(f'hm = {hm} hm')
print(f'dam = {dam} dam')
print(f'dm = {dm} dm')
print(f'cm = {c} cm')
print(f'mm = {mm} mm')
