# Ejercicio 9: Eliminar cadenas vacías de una lista.

lista_cadenas = ["Hola", "", "Python", "", "Mundo"]
filtradas = [cadena for cadena in lista_cadenas if cadena]

print("Lista sin cadenas vacías:", filtradas)
