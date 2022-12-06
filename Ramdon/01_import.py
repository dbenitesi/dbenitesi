#   Process to import module
# Importamos el módulo random para seleccionar una palabra al azar
import random

# Definimos una lista de palabras posibles
palabras = ["gato", "perro", "pez", "elefante", "rana"]

# Seleccionamos una palabra al azar
palabra_secreta = random.choice(palabras)

# Creamos una lista con "_" en lugar de las letras de la palabra secreta
palabra_oculta = ["_" for letra in palabra_secreta]

# Inicializamos un contador para llevar la cuenta de los intentos fallidos
intentos_fallidos = 0

# Mientras queden intentos y la palabra no se haya adivinado
while intentos_fallidos < 10 and "_" in palabra_oculta:
  # Mostramos la palabra oculta
  print(" ".join(palabra_oculta))
  # Pedimos al usuario que adivine una letra
  letra = input("Adivina una letra: ")
  # Comprobamos si la letra está en la palabra secreta
  if letra in palabra_secreta:
    # Si está, la añadimos a la palabra oculta en su posición correspondiente
    for i in range(len(palabra_secreta)):
      if palabra_secreta[i] == letra:
        palabra_oculta[i] = letra
  else:
    # Si no está, aumentamos el contador de intentos fallidos
    intentos_fallidos += 1

# Si se adivinó la palabra, mostramos un mensaje de felicitación
if "_" not in palabra_oculta:
  print("¡Felicidades! Adivinaste la palabra: " + "".join(palabra_oculta))
else:
  # Si se agotaron los intentos, mostramos un mensaje de derrota
  print("¡Lo siento! No adivinaste la palabra. La palabra era: " + palabra_secreta)
