"""Crie um programa que tenha uma tupla única como nomes de produtos  e seus respectivos preços, na sequência. No
final, mostre uma listagem de preços, organizando os dados em forma tabular. """

tu = tuple()
nome = str(input('Qual o nome do seu estabelecimento? ')).upper().lstrip().rstrip()
print('Agora, insira quantos  produtos quiser!')
while True:
    prod = str(input("Nome do produto: ")).capitalize().lstrip().rstrip()
    val = float(input('Valor do produto: R$'))
    tu += prod, val
    res = str(input('Iserir novo produto? [S/N]')).strip().upper()[0]
    while res not in 'SN':
        res = str(input('Opção inválida! Iserir novo produto? [S/N]')).strip().upper()[0]
    if res == 'N':
        break
print(f'\n{"-" * 40}')
print(f'{nome:^40}')
print('-' * 40)
for pos in range(0, len(tu)):
    if pos % 2 == 0:
        print(f'{f"{tu[pos]} ":.<20}', end='')
    else:
        print(f' $ {tu[pos]:>3.2f}')
print('-' * 40)

# Escrevi esse código mais dinamico, deixando o usuário personaizar nome do estabeleciomento e preencher quantos
# produtos com preço ele quiser. Por enquanto, esse código só tem um problema que eu ainda não consegui resolver,
# quando você deixa vazia a pergunta de quer inserir? o programa dá um erro e para, não consegui resolver isso e
# postei nos comentários para ver se alguém me ajuda. 07/03/2022 12:13
