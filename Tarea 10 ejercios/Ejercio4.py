# Ejercicio 4: Buscar si una subcadena está presente en cada cadena de la lista.

lista_cadenas = ["Cometa", "Nebulosa", "Asteroide", "Quasar", "Supernova"]
subcadena = input("Ingrese la subcadena a buscar: ")
resultados = []

for cadena in lista_cadenas:
    resultados.append(subcadena in cadena)

print("Resultados de búsqueda:", resultados)
