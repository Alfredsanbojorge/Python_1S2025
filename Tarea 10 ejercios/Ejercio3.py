# Ejercicio 3: Convertir cadenas a mayúsculas si su longitud es par, o a minúsculas si es impar.

lista_cadenas = ["Hola", "mundo", "esto", "es", "Python"]
modificadas = [cadena.upper() if len(cadena) % 2 == 0 else cadena.lower() for cadena in lista_cadenas]

print("Cadenas modificadas:", modificadas)
