"""
Tienes dos listas de números, lista_a y lista_b, ambas de la misma longitud. 

Cada número en lista_a se "enfrenta" al número en la misma posición en lista_b.

- Si el número en lista_a es mayor, su valor se suma al siguiente número en lista_a.
- Si el número en lista_b es mayor, su valor se suma al siguiente número en lista_b.
- Si los dos números son iguales, ambos se eliminan y no afectan al siguiente par.

Debes simular estos enfrentamientos y devolver el resultado final:
- Si al final queda un número en lista_a, devuelve ese número seguido de la letra "a" (por ejemplo, "3a").
- Si al final queda un número en lista_b, devuelve ese número seguido de la letra "b" (por ejemplo, "2b").
- En caso de empate, devuelve la letra "x".

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]

resultado = battle(lista_a, lista_b)  # -> "2b"

# Explicación:
# - 2 vs 3: gana 3 (+1)
# - 4 vs 3+1: empate
# - 2 vs 4: gana 4 (+2)
# Resultado: "2b"

lista_a = [4, 4, 4]
lista_b = [2, 8, 2]

resultado = battle(lista_a, lista_b)  # -> "x"

# Explicación:
# - 4 vs 2: gana 4 (+2)
# - 4+2 vs 8: gana 8 (+2)
# - 4 vs 2+2: empate
# Resultado: "x"
"""

lista_a = [1, 2, 4]
lista_b = [1, 4, 1]

def battle_count(lista_a, lista_b):
  residuo = {"a": 0, "b": 0}

  for i in range(len(lista_a)):
    a, b = lista_a[i] + residuo["a"], lista_b[i] + residuo["b"]
    dif = a - b
    if dif > 0:
      residuo.update({"a": dif, "b": 0})
      print(f"Batalla {i + 1}, gano A, con diferencia de {dif}\n")
    elif dif < 0:
      residuo.update({"a": 0, "b": -dif})
      print(f"Batalla {i + 1}, gano B, con ventaja de {-dif}\n")
    else:
      print(f"Batalla {i + 1}, empate de a: {a}, b: {b}\n")

  if residuo["a"] == residuo["b"]:
    resultado = "Empate"
  elif residuo["a"] > residuo["b"]:
    resultado = "A" + str(residuo["a"])
  else:
    resultado = "B" + str(residuo["b"])

  return f"El ganador fue: {resultado}"

    

print(battle_count(lista_a, lista_b))