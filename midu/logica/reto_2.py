eggs = [2, 4]

def contador_huevos_pares(lista):
  huevos_pares = 0
  for huevos in lista:
    if huevos % 2 == 0:
      huevos_pares += huevos
  return huevos_pares
  

print(contador_huevos_pares(eggs))