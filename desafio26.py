##026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a
# letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

nome=str(input('Digite seu nome: ')).upper().strip()
print(len(nome))
x=nome.count('A',0,)
position=nome.find('A')+1
pospos=nome.rfind('A')+1
div=nome.split()
print(f'Quantas vezes aparece a letra (A) em {div}? Aparecem: {x}')
print(f'A letra (A) aparece primeiro na posição: {position} e por último na posição: {pospos}')

#OUUUUU

frase=str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('A posição que ela aparece é {}.'.format(frase.find('A')+1))
print('A ultima posição que aparece é {}'.format(frase.rfind('A')+1))