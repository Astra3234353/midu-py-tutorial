def reto(str):
  r = str.count("R") + str.count("r")
  j = str.count("J") + str.count("j")
  return r == j

print(reto("rRJ"))