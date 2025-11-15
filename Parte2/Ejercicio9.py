contador = 10

while contador >= 1:
  print(f"Contador regresivo: {contador}")
  contador -= 1

print("¡Feliz Año Nuevo!")

suma = 0

numero = int(input("Ingresa un número entero positivo (o negativo para terminar): "))

while numero >= 0:
  suma += numero
  numero = int(input("Ingresa un número entero positivo (o negativo para terminar): "))

print(f"La suma de los números ingresados es: {suma}")