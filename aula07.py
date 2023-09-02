n1= int(input('Digite um valor: '))
n2= int(input('Digite outro valor: '))
nome=input('Qual o seu nome?')
print('Prazer{}! '.format(nome))
print(f'Prazer! {nome:=^20}') # o = vai aparecer em 20 caracteres,
#o ^vai centralizar o nome. < pra esquerda, > pra direita.
print('Prazer {:=^20}'.format(nome))
s=n1+n2
m=n1*n2
d=n1/n2
sub=n1-n2
print(f' O resultado dos números são soma {n1+n2}')
print(f' A multiplicação {n1*n2}', end=',')
print(f' A divisão {n1//n2}, subtração {n1-n2}')
print('='*10)
#end='' para subir a linha
# \n fazer quebra de linha pra baixo
# {:.3f} pra deixar a divisão com 3 casas decimais ex: 1.333 divisão
#print('='*20
