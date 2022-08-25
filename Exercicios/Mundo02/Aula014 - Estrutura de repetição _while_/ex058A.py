"""Melhore o jogo do desafio 28 onde o computador vai 'pensar' em um número de 0 a 10. Só que agora o jogador
vai tentar adivinhar até acertar. Mostrando no final quantos palpites foram necessários para vencer."""
from random import randint
print('Vou pensar em um número de 0 a 10. Consegue adivinhar?')
nc = randint(0, 10)  # Escolha do computador
nu = int(input('Em qual número eu pensei? '))  # Escolha do usuário
if nu == nc:
    print(F'Parabéns, você venceu! Eu pensei no número {nc}')
cp = 1  # contador de palpites
while nu != nc:
    cp += 1
    if nu < nc:
        nu = int(input('VOCÊ ERROU!\n'
                       'Vou te dar outra chance, mas dessa vez tente um número MAIOR!\n'
                       'Qual número eu pensei? '))
    else:  #elif nu > nc: # tanto o else quanto o elif tem o mesmo efeito nesse caso
        nu = int(input('VOCÊ ERROU!\n'
                       'Vou te dar outra chance, mas dessa vez tente um número MENOR!\n'
                       'Qual número e pensei? '))
if cp > 1:
    print(f'\nVocê acertou em {cp} tentativas o número que eu pensei foi {nc}')

# Vi o programa do professor rodando no começo do vídeo e antes de ver o código dele, reescrevi da mesma forma que fiz antes,
# mas dando dicas pro usuário se o número precisa ser MAIOR ou MENOR 21/02/2022 16:12
