'''Escreva um programa que faça o computador "pensar" em um número inteiro de 0 a 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador. o programa deverá escrever na tela se o usuário
venceu ou perdeu.'''
import random
from time import sleep

print('\033[33m==|==|\033[m' * 13)
print('\033[1;33;40mVou pensar em um número  de 0 a 10. Consegue adivinhar?\033[m')
sleep(2)
print('\033[33m==|==|\033[m' * 13)
c = random.randint(0, 10)
j = int(input('\033[1;33;40mQual número eu pensei?\033[m '))
print('\033[1;36mPROCESSANDO...\033[m')
sleep(2)
m1 = ('seu merda')
m2 = ('você é uma decepção')
m3 = ('até meu saco é mais intuitivo que você')
m4 = ('seus pais te acham um fracasso total')
m5 = ('já vi pessoas em manicomios mais intuitivas que você')
l = [m1, m2, m3, m4, m5]
m = random.choice(l)
if c == j:
    print('\033[1;33;40mVocê conseguiu me vencer. Parabéns.\033[m')
else:
    print(f'\033[1;30;41mEu pensei em {c} e não em {j}... Você perdeu, {m}!\033[m')
