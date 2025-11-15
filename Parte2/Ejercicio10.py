nombre = "david"
apellido = "gOmez"
frase = "Hola Esta Es una Frase"

longitud = len(nombre)
print(f"La longitud de tu nombre es: {longitud}")

print(apellido[3])

palabras = frase.split()
print(palabras)

mayusculas = apellido.upper()
print(mayusculas)

texto = apellido.lower()
print(texto)

mensaje = "Hola, Mundo"
cambio = mensaje.replace("Mundo", "Python")
print(cambio)

for x in apellido:
  print(x)