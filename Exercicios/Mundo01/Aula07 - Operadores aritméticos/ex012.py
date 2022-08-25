#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
p = float(input('Valor  do produto: R$'))
print(f'Valor do produto com 5% de  desconto: R${p-(p*0.05):.2f}\n')

print('TESTANDO OUTRA FORMA\n')

#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
p = float(input('Valor  do produto: R$'))
d = float(input('Porcentagem(%) de desconto: '))
pd = p - (p * d/100)
print(f'O preço do seu produto é R${p:.2f}, na promoção com {d:.2f}% de desconto você irá  pagar somente R${pd:.2f}')