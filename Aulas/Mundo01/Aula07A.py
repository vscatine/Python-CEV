n1 = int(input('1º Valor:'))
n2 = int(input('2º Valor:'))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1**n2
print(f'A soma vale {a} \na subtração vale {s} \no produto é {m} \n2a divisão vale {d:.3f}', end=' ')
print(f'Divisão inteira  vale {di} e a potência vale {p}')
