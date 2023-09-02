## Escreva um programa que leia a velocidade de um carro.
## Se ele ultrapassar 80kmh, mostre uma mensagem dizendo que ele foi multado.
## A multa vai custar 7R$ por km acima do limite.
v=(int(input('O carro passou em qual velocidade? ')))
vlimite= 80
multa0=v-vlimite
multa=(v-vlimite)*7
if v <= vlimite:
    print(f'Você está dentro do limite de velocidade {vlimite}, cuidado!')
else:
    print(f'Você ultrapassou o limite de \033[31m{vlimite}Km\033[m e será multado em \033[4;30;41m7,00R$\33[m \33[4mpor Km excedido\33[m!!!')
    print('Você ultrapassou \033[31m{}Km\033[m do limite e a multa vai custar \033[31m{}R$\033[m.'.format(multa0,multa))
    print('\33[36m-=-\33[m' * 20)
    print(f'\033[4;30;107mOBS:\033[m O cálculo referente a multa é: \33[35m{v}-{vlimite}*7={multa}R$\33[m')
#\33[0;33;41m
#\33[4;0;42m  \033[m