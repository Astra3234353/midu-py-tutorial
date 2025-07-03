user_num = -1

while user_num < 0:
  try:
    user_num = int(input("Dame un numero positivo\n"))
    if user_num < 0:
      print(f"el numero que has elegido es: {user_num}, eso no es positivo...")
  except:
    print("Introduce un numero!")

print(f"el numero que has elegido es: {user_num}")