###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]

secreto = mensaje[7:]
print(secreto)
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
numeros = [10, 20, 30, 40, 50]

numeros[0], numeros[-1] = numeros[-1], numeros[0]
print(numeros)
# Intercambia la primera y la última posición utilizando solo asignación por índice.

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

sanwich = pan + ingredientes + pan_abajo
print(sanwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

lista_nueva = lista + lista

print(lista_nueva)
# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
lista = [10, 20, 30, 40, 50]

indice_de_valor_de_enmedio = len(lista) // 2

valor_de_enmedio = lista[indice_de_valor_de_enmedio]

print(valor_de_enmedio)

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
lista = [1, 2, 3, 4, 5, 6] # -> Resultado: [3, 2, 1, 4, 5, 6]

mitad = len(lista) // 2

valor_a_girar = (lista[:mitad])[::-1]
valor_igual= lista[mitad:]

lista_final = valor_a_girar + valor_igual

print(lista_final)