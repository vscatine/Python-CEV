#Condição Simples
n1 = float(input('1ª Nota: '))
n2 = float(input('2ª Nota: '))
m = (n1+n2) / 2
print(f'Sua média foi {m:.1f}')
if m == 10:
    print(f'Parabéns, você tirou nota máxima!')
print('---FIM---')

#Condição composta
n1 = float(input('1ª Nota: '))
n2 = float(input('2ª Nota: '))
m = (n1+n2) / 2
if m >= 6.5:
    (print(f'Parabéns, você passou!'))
else:
    print(f'Infelizmente, você reprovou. Mas não desista, se esforce mais na próxima!')
print('---FIM---')

#Condição simplificada
n1 = float(input('1ª Nota: '))
n2 = float(input('2ª Nota: '))
m = (n1+n2) / 2
print(f'Parabéns! sua média foi {m:.1f}'if m >= 6.5 else f'Se esforce mais na próxima. Sua média foi {m:.1f}')
print('---FIM---')
