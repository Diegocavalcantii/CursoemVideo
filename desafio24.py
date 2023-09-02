#Crie um programa que leia o nome de uma cidade
#e diga se começa ou não com o nome ''SANTO''.

nome=str(input('Digite o nome da sua cidade: ')).strip()
print(nome[:5].upper() == 'SANTO')



