## Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
num1=int(input('Digite o 1 número para ser analisado: '))
num2=int(input('Digite o 2 número para ser analisado: '))
num3=int(input('Digite o 3 número para ser analisado: '))
print('Qual o maior número e qual o menor número? !!!Analisando!!!!')
menor=num1
if num2<num1 and num2<num3:
    menor=num2
if num3<num1 and num3<num2:
    menor=num3

maior=num1

if num2>num1 and num2>num3:
    maior=num2
if num3>num1 and num3>num2:
    maior=num3
print(f'menor valor foi {menor}')
print(f'maior valor foi {maior}')


