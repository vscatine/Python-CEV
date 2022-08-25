"""Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."""
"""c = soma = 0
n = int(input('Digite um número: '))
maior = n
menor = n
resposta = 'S'
while resposta == 'S':
    while n != 999:
        c += 1
        soma += n
        media = soma / c
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        n = int(input('Digite um número: '))
    print(f'Soma = {soma}\n'
          f'Média = {media}\n'
          f'Maior = {maior}\n'
          f'Menor = {menor}')
    resposta = str(input('Quer incluir mais números? [S/N] ')).strip().upper()
    if resposta == 'S':
        n = int(input('Digite um número: '))
    elif resposta == 'N':
        print('FINALIZANDO...')
print('Programa finalizado. Volte Sempre!')
"""
"""# Fiz esse programa antes de ver a resolução do professor. Ficou muito bom, só não consegui fazer funcionar o else,
# caso o usuário digite algo diferente de S ou N na pergunta de inserir mais números. O programa também está um
# pouco feio, mas esse não era meu foco no momento. Vou ver a resolução do professor, verificar se tem como resolver
# o problema que eu apresentei a cima e depois vou reescrever, deixando mais bonito e organizado. 24/02/2022 16:03
print('\nPRÓXIMO PROGRAMA\n')
n = int(input('Digite um valor: '))
r = str(input('Quer continuar? [S/N] ')).strip().upper()
c = 1
soma = n
maior = n
menor = n
media = 0
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    soma += n
    c += 1
    media = soma / c
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'C = {c} e soma = {soma} e média = {media} e maior = {maior} e menor = {menor}')
print(f'Você digitou {c} números, a soma entre eles foi {soma},\n'
      f'a média foi {media}, o menor valor foi {menor} e o maior valor foi {maior}')"""

# Vi os primeiros segundos do vídeo e o programa do professor estava diferente do meu, mas com uma funcionalidade igual.
# O dele estava perguntando se o usuário quer continuar após cada número inserido e o meu estava funcionando em blocos de números.
# Então decidi reescrever antes de ver o vídeo eo código  do professor. Para chegar numa resultado próximo do dele.
# Consegui fazer, mas usando aquela gambiarra e colocar o contador com 1, não sei se ele fez igual
# agora vou ver a resolução e ver código para ver se melhoro algo. 24/02/2022 16:28
# Na verdade eu vi que minha media não está certa, vou refazer. Já vi o vídeo do professor 16:51
