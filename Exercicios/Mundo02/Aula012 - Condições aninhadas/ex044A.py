"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros"""
print(f'{" LOJAS VITOR ":=^40}')
p = float(input('Valor total: R$'))
print('FORMAS DE PAGAMENTO:\n'
      '[ 1 ] à vista dinheiro/cheque\n'
      '[ 2 ] à vista no cartão\n'
      '[ 3 ] 2x no cartão\n'
      '[ 4 ] 3x ou mais no cartão (20% de juros por parcela)')
f = int(input('Qual a forma de pagamento? '))
print()
if f == 1:
    d = p * 0.1
    print(f'10% de desconto para pagamento a vista no dinheiro ou cheque!\n'
          f'Valor do desconto: R${d:.2f}\n'
          f'Valor total: R${p - d:.2f}')
elif f == 2:
    d = p * 0.05
    print(f'5% de desconto para pagamento à vista no cartão!\n'
          f'Valor do desconto R${d:.2f}\n'
          f'Valor total: R${p - d:.2f}')
elif f == 3:
    print(f'Pagamento  em 2x no cartão.\n'
          f'Valor total: R$ {p:.2f}')
elif f == 4:
    print('Pagamento  em 3x ou mais no cartão (20% de juros por parcela).')
    qp = int(input('Quantas parcelas? '))
    vp = p / qp + (p / qp * 0.2)
    print(f'Valor da parcela: R${vp:.2f}\n'
          f'Valor total: R${vp * qp:.2f}')
else:
    print('OPÇÃO INVÁLIDA!')
