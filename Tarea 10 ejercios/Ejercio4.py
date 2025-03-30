# Ejercicio 4: Buscar si una subcadena está presente en cada cadena de la lista.

lista_cadenas = ["Hola", "mundo", "esto", "es", "Python"]
subcadena = input("Ingrese la subcadena a buscar: ")

resultados = [subcadena in cadena for cadena in lista_cadenas]

print("Resultados de búsqueda:", resultados)
