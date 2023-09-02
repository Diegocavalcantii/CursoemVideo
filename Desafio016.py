#desafio16
from math import floor
num=float(input('Digite um número: '))
print(f' O número {num} na sua parte inteira é: {floor(num)}')

#desafio19 Um professor quer sortear um dos seus alunos.
#faça um programa que leia o nome ela e mostre o escolhido.
import random
print('Digite o nome do aluno participante: ')
a1=input('Participante 1: ')
a2=input('Participante 2: ')
a3=input('Participante 3: ')
a4=input('Participante 4: ')
r1=(a1,a2,a3,a4)
r2=random.choice(r1)
print(f' O participante sorteado foi {r2}')

#desafio20 O professor que sortear a ordem de apresentação dos 4 alunos.
#Faça um programa que leia os nomes e determine a ordem dos 4 alunos.

import random
print('Digite o nome dos alunos para ordem dos trabalhos: ')
r1=str(input('Nome do primeiro aluno: '))
r2=str(input('Nome do segundo aluno: '))
r3=str(input('Nome do terceiro aluno: '))
r4=str(input('Nome do quarto aluno: '))
sorteio=[(r1),(r2),(r3),(r4)]
ordem=(random.sample(sorteio,4))
print(f'A ordem de apresentação será: {ordem}')
print('A ordem foi: {}' .format(ordem))

