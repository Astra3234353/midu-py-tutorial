persona = {
  "nombre": "Alex",
  "Edad": 18,
  "Calificaciones": [8, 9, 9],
  "es_estudiante": True
}

persona["nombre"] = "Julian"

es_estudiante = persona.pop("es_estudiante")

print(persona.keys())


list = [1, 4, 7, 9]
goal = 16

def path_finder(list, goal):
  seen = {}
  for i, value in enumerate(list):
    need = goal - value
    if need in seen: 
      return f"i:{i}, j:{seen[need]}"
    seen[value] = i

print(path_finder(list, goal))
