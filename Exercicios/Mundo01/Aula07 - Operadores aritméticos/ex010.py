#Crie um programa que leia quanto  dinheiro uma pessoa tem na carteira e quantos dólares ela pode comprar.
# Considere US$1.00 = R$3.27
r=float(input('Quanto dinheiro você tem na carteira? R$'))
d=float(r/3.27)
print(f'Com R${r:.2f} você pode comprar US${d:.2f}')


#Crie um programa que leia quanto  dinheiro uma pessoa tem na carteira e quantos dólares ela pode comprar.
# Considere US$1.00 = R$3.27
r=float(input('Quantos R$ você tem na carteira?'))
print(f'Com R${r:.2f} você pode comprar US${r/3.27:.2f}')
