"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros"""
print('=' * 10, 'LOJAS VITOR', '=' * 10)
pn = float(input('Valor do produto: R$'))
p1 = pn - (pn * 0.1)
p2 = pn - (pn * 0.05)
f = int(input(f"""Qual a forma de pagamento?
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no  cartão
Qual é a opção? (preencha com 1, 2, 3 ou 4): """))
print()
if f == 1:
    print(f'Desconto de 10%: R${pn * 0.1:.2f}')
    print(f'Valor total: R${p1:.2f}')
elif f == 2:
    print(f'Desconto de 5%: R${pn * 0.05:.2f}')
    print(f'Valor total: R${p2:.2f}')
elif f == 3:
    print(f'Valor total: R${pn:.2f}')
elif f == 4:
    pa = int(input('Quantas parcelas? '))
    vp = (pn / pa) + (pn / pa * 0.2)
    print(f'Você irá pagar {pa} parcelas de {vp:.2f}')
    print(f'Valor total com 20% de juros por parcela: R${vp*pa:.2f}')
else:
    print('OPÇÃO INVÁLIDA. Tente novamente.')
