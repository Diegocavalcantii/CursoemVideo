import random

# criar lista de arrays aleatórios com números de 1 a 30
array_list = []
for i in range(30):
    array = [random.randint(1,30) for j in range(30)]
    array_list.append(array)

# criar lista com todos os números, incluindo os repetidos
all_numbers = [number for array in array_list for number in array]

# criar lista com apenas os números repetidos
repeated_numbers = []
for number in all_numbers:
    if all_numbers.count(number) > 1 and number not in repeated_numbers:
        repeated_numbers.append(number)

# imprimir as duas listas
print("Lista com todos os números gerados: ", all_numbers)
print("Lista com apenas os números repetidos: ", repeated_numbers)