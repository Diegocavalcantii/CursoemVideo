## Desenvolva um programa que pergunte a distância de uma viagem em Km.
## Calcule o preço da passagem, cobrando R$ 0,50 por km
## para viagens de até 200km e R$0,45 para viagens mais longas.

dist=float(input('Qual a distância da sua viagem? '))
valor1=0.50*dist
valor2=0.45*dist
if dist <= 200:
    print(f'O valor da viagem custará: R${valor1:.2f}')
else:
    print(f'O valor da viagem custará: R${valor2:.2f}')

