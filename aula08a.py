import math
num=int(input('Digite um número: '))
raiz=math.sqrt(num)
print(f'A raiz quadrada do número {num} é igual a {raiz}')
from math import log2
num=int(input('Digite outro número: '))
log=log2(num)
print('A raiz de {} é igual {}'.format(num,log))

import random
num=random.randint(1,10)
print('O numero aleatório é {}'.format(num))

import emoji
print(emoji.emojize('Olá, mundo :grinning_face:', use_aliases=))
