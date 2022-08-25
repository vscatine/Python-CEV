# Variáveis compostas (Tuplas)
# Tuplas começam entre parenteses ()
# Tupla são imutáveis
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print('Usando for com len:')
for cont in range(0, len(lanche)):
    print(f'Eu comi {lanche[cont]} na posição {cont}')

print('\nUsando o for:')
for comida in lanche:
    print(f'Eu comi {comida}')

print('\nUsando o for com enumerate:')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('\nUsando o sorted:')
print(sorted(lanche))
print(lanche)

print('\nNOVA TUPLA')
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.count(5))
print(c.index(5))
print(c.index(5, 1))

print('\nNova tupla')
pessoa = ('Vitor', 27, 'M', 82.3)
for dados in pessoa:
    print(f'Meu nome é {dados}')
print(f'\nMeu nome é {pessoa[0]}, tenho {pessoa[1]} anos, sou do sexo {pessoa[2]} e peso {pessoa[3]}')
