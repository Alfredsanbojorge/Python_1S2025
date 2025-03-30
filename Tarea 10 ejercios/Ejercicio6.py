# Ejercicio 6: Eliminar espacios en blanco al inicio y al final de cada cadena.

lista_cadenas = ["  Hola  ", "  mundo", "Python  "]
limpias = [cadena.strip() for cadena in lista_cadenas]

print("Cadenas sin espacios:", limpias)
