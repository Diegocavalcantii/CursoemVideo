n1=int(input('Digite um numero: '))
n2=int(input('Digite outro numero: '))
n3=(input('Digite algo: '))
soma= n1+n2
print('A soma entre os números {0} e {1} é: {2}'.format(n1, n2, soma))
print(type(n3))
print('É um número?', n3.isalnum())
print('É um número?', n3.isnumeric())
print('É um titulo?', n3.istitle())


