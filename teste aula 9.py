frase='  Curso em Vídeo Python  '
print(frase) #imprime a frase
print(frase[3]) #.. a posição 3 's')
print(frase[3:13]) #.. a posição 3 até 12
print(frase[:13]) #.. posição 0 'C' até o 12
print(frase[1:16]) #.. posição 1 'u' até o 15 'P'
print(frase[1:16:2]) #.. posição 1 'u' até 15'P' de 2 em 2
print(frase.count('O')) #.. contagem de quantos 'o' tem.
print(frase.upper().count('O')) # torna caixa alta todos os 'o' e faz contagem.
print(len(frase)) #diz a contagem da string
print(len(frase.strip())) #retira os espaços indesejados
print(frase.replace('Python','Android')) #substituição de pytron por android
# caso eu queira uma troca permanente
frase=frase.replace('Python','Android')
print('Curso' in frase) #mostra se curso está em frase
print(frase.find('Vídeo')) #encontra a posição que inicia vídeo
print(frase.lower().find('vídeo')) #transformou em pequeno e localizou a posição
dividido=frase.split()
print(dividido[3][2])#mostra a partição 3 e 2 letra Vídeo D.

