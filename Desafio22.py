#022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.


nome=str(input('Diga seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print(f'O seu nome completo possui', {len(nome)-nome.count(' ')}, 'letras')
print(f' O seu primeiro nome poussi', {nome.find(' ')}, 'letras')
dividido=nome.split()
print(f'O nome {dividido[0]} possui {len(dividido[0])} letras')

