'''Crie um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A"
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a últiima  vez.'''
f = input('Digite uma frase: ').upper().strip()
print(len(f))
print(f'A letra "A" aparece {f.count("A")} vezes na frase.')
print(f'A letra "A" aparece na posição {f.find("A")+1} pela primeira vez na frase.')
print(f'A letra "A" aparece na posição {f.rfind("A")+1} pela última vez na frase.')