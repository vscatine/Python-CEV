"""Melhore o jogo do desafio 28 onde o computador vai 'pensar' em um número de 0 a 10. Só que agora o jogador
vai tentar adivinhar até acertar. Mostrando no final quantos palpites foram necessários para vencer."""
from random import randint

print('Vou pensar em um número de 0 a 10... Consegue adivinhar?')
nc = randint(1, 10)
acertou = False
cp = 0  # Contador de palpites
while not acertou:
    nu = int(input('Em que número eu pensei? '))
    cp += 1
    if nu == nc:
        acertou = True
    else:
        if nu > nc:
            print('ERROU!\n'
                  'Vou te dar mais uma chance, só que dessa vez escolha um número MENOR!')
        else:
            print('ERROU!\n'
                  'Vou te dar mais uma chance, só que dessa vez escolha um número MAIOR!')
if cp == 1:
    print(f'Você venceu de primeira... PARABÉNS!')
else:
    print(f'Você acertou em {cp} tentativas')

# Escrevi esse código baseado na forma como o professor resolveu. Não gostei muito dessa forma,
# mas de qualqer forma é importante ver como se faz de outro jeito. 21/02/2022 16:49
