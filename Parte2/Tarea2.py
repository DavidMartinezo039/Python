numero = int(input("Introduce un número entero:"))

match numero:
  case numero if numero < 0:
    print("El número es menor que cero")
  case numero if numero >= 0 and numero < 10:
    print("El número es mayor o igual a 0 y menor que 10")
  case _:
    print("El número es mayor o igual que 10")

# Recibir un valor númerico entero
# Comrobar si es menor que cero
# Si es mayor o igual que cero y menor que 10
# Si es mayor que 10