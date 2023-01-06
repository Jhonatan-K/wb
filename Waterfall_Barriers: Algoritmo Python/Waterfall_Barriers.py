# hallar el indice del valor máximo y valor mínimo
def find_next_max(curr_idx, current_list):
    current_value = current_list[curr_idx] # valor en el indice dentro de la lista
    for i, v in enumerate(current_list):
        if (i <= curr_idx):
            continue
        if (v > current_value):
            return [i, v]
        
    return [-1, -1] # retornar un indices inexistentes
#
#
def calculate_total(start,end):
    total = 0 # para partir de 0
    # print('calculate_total', start, end)
    s = min(start, end) ## inicio del rango 
    e = max(start, end) ## fin del rango
    list = [] # lista vacía donde irán los valores filtrados
    for i,v in enumerate(barriers): # filtrar valores por indices <<
        if i < s: # ignorar lo que este antes del principio
            continue
        if i > e: # ignorar lo que este después del final
            break
        list.append(v) # filtrando lista 
        
    if (start > end):
        list.reverse() # invertir el orden de la lista en caso de que el indice start sea mayor que end
    #9-8-5-1    
    jump = 0
    for i,c in enumerate(list):
        if i <= jump: # para tener un previo y un actual y comparar con
            continue
        p = list[i-1] # p valor en indice anterior al indice actual
        next_max_value = find_next_max(i, list) # <<<<<<<<<
        if next_max_value[0] > -1: # en el caso de escaleras con desniveles (9,4,2,8,1)
            spaces = (next_max_value[0] - i) + 1 # se suma 1 para contar el espacio inicial
            total += next_max_value[1] * spaces # para saltar un valor menor y multiplicar el siguiente
            jump = next_max_value[0]
        else:
            total += min(c, p) # agrega al contador total el valor menor entre c y p
    
    return total # total de agua maxima 
#    
#
#
# Lista inicial <<
barriers = [1,5,8,9,4,5]
#
#
print(barriers)
print()
#
#
# Valores mínimos y máximos con sus indices
max_value = None
max_value_index = None
min_value = None
min_value_index = None
#
#
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
#
# total = a la función de encontrar el total de agua maxima a partir de indices mínimos y máximos <<
total = calculate_total(max_value_index, min_value_index)
print()
# Resultados de hallazgo de mínimos y máximos <<
print(f'{max_value_index} es el la posición maxima y {max_value} es el valor máximo\n{min_value_index} es la posición minima y {min_value} es el valor mínimo')
print()
print(f'{total} es la capacidad maxima de agua entre {max_value} y {min_value}')
##
##                 
##
##
