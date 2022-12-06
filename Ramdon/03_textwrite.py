# Definimos la cadena de texto original.
original_string = "HONOR es lo que se gana"

# Pedimos al usuario que introduzca la palabra que quiere utilizar para reemplazar "HONOR".
new_word = input("Introduce la palabra que quieres utilizar para reemplazar 'HONOR': ")

# Utilizamos la función `str.replace` para reemplazar "HONOR" por la palabra introducida por el usuario.
modified_string = original_string.replace("HONOR", new_word)

# Utilizamos la función `open` para crear un archivo de texto y escribir la cadena modificada en él.
# Si el archivo ya existe, se sobrescribirá.
with open("modified_string.txt", "w") as file:
    file.write(modified_string)

# Mostramos al usuario la cadena modificada para confirmar que se ha realizado correctamente el reemplazo.
print(f"Cadena modificada: {modified_string}")
