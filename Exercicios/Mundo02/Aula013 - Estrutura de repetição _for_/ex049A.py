""" Refaça o exercício 009, mostrando a tAbuada de um númer o que o usuário escolher, só que agora
utilizando um LAÇO FOR."""
n = int(input('Digite um número para ver a sua tabuada: '))
for c in range(1,11):
    print(f'{n:2} x {c:2} = {n * c:2}')

'''Depois de ver a resolução do professor vi que eu estava usando um contador redundante. 
mesmo assim tive um bom resultado sozinho e aprimorei com a forma do professor. 16/02/2022 15:11'''