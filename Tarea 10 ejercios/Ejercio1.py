# Ejercicio 1: Concatenar todas las cadenas de una lista en una sola, separadas por un espacio.

lista_cadenas = ["Bienvenido", "al", "universo", "de", "Python"]
resultado = ""

for cadena in lista_cadenas:
    resultado += cadena + " "

resultado = resultado.strip()  # Eliminar el espacio extra al final
print("Cadena concatenada:", resultado)
