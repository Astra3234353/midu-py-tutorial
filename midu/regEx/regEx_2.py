import re

text = 'hola.txt xd.txt  Ihateyou.txt.bat .'
pattern = r'.txt\b|'

result = re.findall(pattern, text)

print(result)