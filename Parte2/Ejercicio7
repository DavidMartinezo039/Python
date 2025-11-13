numero = int(input("Introduce un número entero:"))

match numero:
  case 0:
    print("El número es un cero")
  case numero if numero % 2 == 0:
    print("El número es par")
  case numero if numero % 2 != 0:
    print("El número es impar")
  case _:
    print("No es válido")

# En este ejercicio el último case nunca se podrá cumplir

match numero:
  case 0:
    print("El número es un cero")
  case _ if numero % 2 == 0:
    print("El número es par")
  case _:
    print("El número es impar")

# Este otro ejemplo estaría mejor