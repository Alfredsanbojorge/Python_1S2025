# Ejercicio 9: Eliminar cadenas vacías de una lista.

lista_cadenas = ["Hola", "", "Python", "", "Mundo"]
filtradas = []

for cadena in lista_cadenas:
    if cadena:
        filtradas.append(cadena)

print("Lista sin cadenas vacías:", filtradas)
