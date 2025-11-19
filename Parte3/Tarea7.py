"""
Descripción:



Escribe un programa en Python que permita al usuario ingresar su nombre, edad, dirección y número de teléfono, y luego muestre estos datos en pantalla.



Instrucciones:



   1 Crea un diccionario llamado datos_personales con las siguientes claves: "nombre", "edad", "direccion" y "telefono". Inicializa todos los valores a None.

   2 Solicita al usuario que ingrese su nombre, edad, dirección y número de teléfono y almacena cada valor en el diccionario datos_personales.

   3 Muestra en pantalla los datos ingresados por el usuario utilizando las claves del diccionario
"""

datos_personales = {
  "nombre": None,
  "edad": None,
  "direccion": None,
  "telefono": None,
}

datos_personales["nombre"] = input("Introduce tu nombre: ")
datos_personales["edad"] = input("Introduce tu edad: ")
datos_personales["direccion"] = input("Introduce tu direccion: ")
datos_personales["telefono"] = input("Introduce tu telefono: ")
print(f"{datos_personales['nombre']} tiene {datos_personales['edad']} años, vive en {datos_personales['direccion']} y su numero de telefono es {datos_personales['telefono']}")