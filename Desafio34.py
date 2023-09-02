salario=float(input('Quanto voce recebe de salário? '))
aumento10= (salario*10/100)
aumento15= (salario*15/100)
if salario <= 1250:
    print(f'O salário terá um aumento de {aumento15} totalizando {salario+aumento15}')
else:
    print(f'O salário terá um aumento de {aumento10}')

#ouuuu de outra forma

if salario<=1250:
    novo=salario+(salario*15/100)
else:
    novo= salario + (salario * 10 / 100)
print('Quem ganhava R$:{:.2f} passa a ganhar {}'.format(salario, novo))