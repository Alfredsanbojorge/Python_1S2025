# Ejercicio 3: Convertir cadenas a mayúsculas si su longitud es par, o a minúsculas si es impar.

lista_cadenas = ["Hola", "mundo", "esto", "es", "Python"]
modificadas = []

for cadena in lista_cadenas:
    if len(cadena) % 2 == 0:
        modificadas.append(cadena.upper())
    else:
        modificadas.append(cadena.lower())

print("Cadenas modificadas:", modificadas)
