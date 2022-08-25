#Condição Simples
n = str(input('Qual é o seu nome? ')).title().strip()
if n == 'Vitor':
    print('Que nome lindo, cara!')
print(f'Bom dia, {n}!')
print('---FIM---')
#Condição composta
n = str(input('Qual é o seu nome? ')).title().strip()
if n == 'Esdras':
    print(f"""{n}, seus pais devem te odiar :/
Mas de qualquer forma, tenha um bom dia, {n}!""")
else:
    print(f'Bom dia, {n}!')
print('---FIM---')

#Condição simplificada
n = str(input('Qual é o seu nome? ')).strip().title()
print(f'Bom dia, {n}!\nVocê é lindão cara'if n == 'Vitor'else f'Bom dia, {n}!')
print('---FIM---')
