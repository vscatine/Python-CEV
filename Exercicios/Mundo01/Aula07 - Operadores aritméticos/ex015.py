#Escreve um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de
#dias pelos quais ele alugado. calcule o preço a pagar, sabendo que o carro custa R$60.00 por dia e R$0.15 por km rodado.

'''kp = float(input('Km percorridos: '))
qd = int(input('Quantidade de dias do aluguel: '))
pd = int(qd*60.00)
pk = float(kp*0.15)
print(f'1 - Dias de aluguel: {qd}\n2 - Km percorridos: {kp:.2f}\n3 - Valor diárias: {pd:.2f}\n4 - Valor Km: {pk:.2f}\n5 - Valor total(3 + 4): {pd+pk}')'''

d = int(input('Quantidade de dias do aluguel:'))
print('Valor por dia: R$60,00')
print(f'Valor por dias alugados: R${d*60:.2f}')
km = float(input('Km percorridos: '))
print('Valor por km percorrido: R$0,15')
print(f'Valor total dos kms percorridos: R${km*0.15:.2f}')
print(f'Valor total a pagar(Dias + kms): R${(d*60)+(km*0.15):.2f}')
