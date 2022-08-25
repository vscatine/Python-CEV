'''Condições'''
#Condição simples
c = int(input('Quantos anos tem seu carro?' ))
if c <= 3:
    print('Seu carro é novo!')
print('---FIM---')

#Condição composta
c = int(input('Quantos anos tem seu carro? '))
if c <= 3:
    print('Seu carro é novo!')
else:
    print("Tá na hora de trocar esse troço velho --'")
print('---FIM---')

#Condição simplificada
c = int(input('Quantos anos tem seu carro? '))
print('Seu carro é novo!'if c<=3 else'Que lata velha!')
