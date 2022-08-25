"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
caso esteja errado, peça a digitação novamente até ter um valor correto."""
s = str(input('Qual o seu  sexo? (M/F) ')).upper().strip()
"""while s == 'M' or s == 'F':
    if s != 'M' or s != 'F':
        print('OPÇÃO INVÁLIDA! Digite M para masculino ou F para feiminino.')"""
# Assisti a aula de while ontem e acabei nao conseguindo fazer nenhum exercício.
# Escrevi  esse código hoje antes de rever a  aula e, obviamente, o código  não está funcionando kkk vou rever a aula e reescrever. 21/02/2022 10:31
s = 'M'
r = 'S' # tentei perguntar se o usuário queria  continuar, pro progrma ter fim, mas deu pau e eu voltei para o que estava funcionando antes.
while s == 'M' or s == 'F':
    s = str(input('Qual o seu sexo(M/F)? ')).strip().upper()
    if s != 'M' and s != 'F':
        print('Opção inválida! Digite M para masculino e F para feminino.')
        s = str(input('Qual o seu sexo(M/F)? ')).strip().upper()
print('Fim')

# Consegui fazer o código funcionar do jeito que o exercício pede, mas não consegui fazer ele parar.
# Tentei perguntar se o usuário quer continuar ou não e aí o programa parou de funcionar, ou seja, o programa funciona, só que eternamente. kkkrying
# Vou ver a resolução do exercício e ver se preciso  aprimorar o código e se o professor tem uma solução pro meu  problema. 21/02/2022 11:28

