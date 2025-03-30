# Ejercicio 6: Eliminar espacios en blanco al inicio y al final de cada cadena.

lista_cadenas = ["  Cohete  ", "  Satélite", "Asteroide  "]
limpias = []

for cadena in lista_cadenas:
    limpias.append(cadena.strip())

print("Cadenas sin espacios:", limpias)
