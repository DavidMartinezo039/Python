personas = (("Juan", 28), ("María", 22), ("Pedro", 35), ("Ana", 30))

for nombre, edad in personas:
  if edad > 18:
    print(f"{nombre} es mayor de edad con {edad} años.")

numeros = (5, 10, 15, 20, 25)

suma = sum(numeros)

print(f"La suma de los números en la tupla es: {suma}")