from random import shuffle
from collections import Counter


# hallar el indice del valor máximo y valor mínimo
def calculate_uneven_staircase(current_index, current_list):
    # en el caso de una escalera irregular
    current_value = current_list[current_index] # valor en el indice dentro de la lista
    for i, v in enumerate(current_list):
        if (i <= current_index):
            continue
        if (v > current_value):
            return [i, v]
    # en un caso como 9-4-5 ignorara el 4 para sumar el total de 9+5+2 espacios= 10    
    return [-1, -1] # retornar un indices inexistentes
#
def filtering_list(start,end):
    total = 0 # para partir de 0
    s = min(start, end) ## s = a Start o inicio 
    e = max(start, end) ## e = a End o fin
    list = [] # lista vacía donde irán los valores filtrados
    
    for i,v in enumerate(barriers): # filtrar valores por indices <<
        if i < s: # ignorar lo que este antes del principio (start)
            continue
        if i > e: # ignorar lo que este después del final (end)
            break
        list.append(v) # filtrando lista [1,5,8,9,4,5] a [1,5,8,9]
    return list
#
def reverse_list(list):
    #[1, 5, 8, 9]
    if (list[-1] > list[0]):
        list.reverse() # invertir el orden de la lista en caso de que el indice start sea mayor que end
    return list # [9, 8, 5, 1]       
#
def calculate_max_water(list):
    # recorrido y suma
    water = 0
    index_jump = 0
    for i,current_index in enumerate(list): # para tener un previo y un actual y comparar
        if i <= index_jump: # la iteración es menor o igual que el salto?
            continue
        previous_index = list[i-1] # previous_index valor en indice anterior al indice actual
        #
        # 
        # en caso de una escalera irregular <==============
        next_max_value = calculate_uneven_staircase(i, list) # <<<<<<<<<
        if next_max_value[0] > -1: # en el caso de escaleras con desniveles (9,4,2,8,1)
            spaces = (next_max_value[0] - i) + 1 # se suma 1 para contar el espacio inicial
            water += next_max_value[1] * spaces # para saltar un valor menor y multiplicar el siguiente
            index_jump = next_max_value[0]            
        else:
            water += min(current_index, previous_index) # agrega al contador total el valor menor entre current index y previous value <-----------------
    return water # total de agua maxima 
#
#
# Lista inicial <<<<<<<<<<<<<<<<<<<<<<
barriers = [1,5,8,9,4,5]
shuffle(barriers)

print(barriers)
print()

# Valores mínimos y máximos con sus indices
max_value = None
max_value_index = None
min_value = None
min_value_index = None

# iterar entre la lista para encontrar mínimos y máximos <<
for i, v in enumerate(barriers): # itero entre indice y valor dentro de la lista <<
    if max_value is None or v > max_value:
        max_value = v
        max_value_index = i
        # mientras el valor mínimo sea none o valor iterado sea mayor que valor máximo, le dare de valor máximo ese valor iterado <<
    if min_value is None or v < min_value:
        min_value = v
        min_value_index = i
        # mientras el valor mínimo sea none o valor iterado sea mayor que valor máximo, le dare de valor máximo ese valor iterado <<

filtered_barriers = filtering_list(max_value_index, min_value_index)

reverse_barriers = reverse_list(filtered_barriers)

max_water = calculate_max_water(reverse_barriers)

print()

# Resultados de hallazgo de mínimos y máximos <<
print(f'{max_value_index} es el la posición maxima y {max_value} es el valor máximo\n{min_value_index} es la posición minima y {min_value} es el valor mínimo')
print()
# resultado final
print(f'{max_water} es la capacidad maxima de agua entre el {max_value} y el {min_value} en la lista {barriers}')

