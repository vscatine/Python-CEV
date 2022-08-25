# código do churros
# Faca um algoritmo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto

# Meu codigo
pv = float(input('Digite o preco antigo do produto: R$'))
nv = pv * 0.95
print(f'O novo preco do produto com 5% de desconto é de R${nv:.2f}')

# Codigo professor
pv = float(input('Digite o preco antigo do produto: R$'))
nv = pv - (pv * 5 / 100)
print(f'O novo preco do produto com 5% de desconto é de R${nv:.2f}')

# Ideia do comentario
pv = float(input('Digite o preco antigo do produto: R$'))
x = float(input('Qual será o desconto em porcentagem? '))
d = (pv/100) * x
nv = pv-d
print(f'O produto que custava R${pv:.2f}, com {x:.2f}% de desconto, vai custar R${nv:.2f}')