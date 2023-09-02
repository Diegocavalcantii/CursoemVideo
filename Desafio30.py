## Crie um programa que leia um número inteiro e mostre na tela se ele é ÍMPAR OU PAR

n=int(input('Digite um número qualquer: '))
resultado=n%2
print(f'Verificando se o número é \033[31mÍMPAR\033[m ou \033[36mPAR\033[m..Aguarde!!!')
if resultado < 1:
    print(f'O número {n} é \033[36mPAR\033[m')
else:
    print(f'O número {n} é \033[31mÍMPAR\033[m')

#ouuu
#pode abrir uma nova variável (uma lista de cores) anexando todos as cores que serão usadas no sistema.
cores = {'ok':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretobranco':'\033[7;30m'}
print('olá! Muito prazer em te conhecer, {}{}{}!!'.format(cores['pretobranco'],n, cores['ok']))
