frutas = ["manzana", "banana", "cereza", "durazno", "kiwi"]
contador = 0

# Bucle for que itera sobre la lista de frutas
for fruta in frutas:
  contador += 1
  print(f"Fruta {contador}: {fruta}")
  if fruta == "cereza":
    print("¡Encontré la cereza! Saliendo del bucle.")
    break
