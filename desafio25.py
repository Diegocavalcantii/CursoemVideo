# #025: Crie um programa que leia o nome
# de uma pessoa e diga se ela tem "SILVA" no nome.

nome=str(input('Digite seu nome: ')).strip()
print('SILVA' in nome.upper())
print(nome.find('SILVA'))
if ('SILVA' in nome) == True:
    print('Você teu o nome Silva.')
else:
    print('Você não tem o nome Silva.')