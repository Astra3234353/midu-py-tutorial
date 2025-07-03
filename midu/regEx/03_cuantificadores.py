###
# 03 - Quantifiers
# Los cuantificadores se utilizan para especificar cuántas ocurrencias de un carácter o grupo de caracteres se deben encontrar en una cadena.
###

import re

# *: Puede aparecer 0 o más veces
text = "aaaba"
pattern = "a*"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio 1:
# ¿Cuantas palabras tienen de 0 a más "a" y después una b?

# +: Una a más veces
text = "dddd aaa ccc a bb aa casa"
pattern = "a+"
matches = re.findall(pattern, text)
print(matches) # ['aaa', 'a', 'aa', 'a', 'a']

# ?: Cero o una vez
text = "aaabacb"
pattern = "a?b"
matches = re.findall(pattern, text)
print(matches) # ['ab', 'b']



# Ejercicio: Haz opcional que aparezca un +34 en el siguiente texto
phone = "+34 688999999"
pattern= r"[\+|00]?\d{1,3}\s?\d{9}"
matches = re.findall(pattern, phone)

print(matches) # ['+34 688999999']
print('arriba \n')

# Ejercicio:
# Encuentra las palabras de 4 a 6 letras en el siguiente texto
words = "ala casa árbol león cinco murcielago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, words)
print(matches)

# Ejercicio
# Encuentra las palabras de más de 6 letras
words = "ala fantastico casa árbol león cinco murcielago"
pattern = r"\b\w{6,}\b"
matches = re.findall(pattern, words)
print(matches)