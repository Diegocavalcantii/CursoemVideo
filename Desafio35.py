print('Voce vai precisar digitar 3 número para formar um triângulo!')
r1=int(input('Digite o 1 segmento: '))
r2=int(input('Digite o 2 segmento: '))
r3=int(input('Digite o 3 segmento: '))
if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print(f'Os segmentos podem formar TRIANGULO')
else:
    print(f'Os segmenos não podem formar TRIANGULO')

