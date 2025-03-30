# Ejercicio 10: Contar cuántas veces aparece un carácter específico en cada cadena.

lista_cadenas = ["Hola", "mundo", "esto", "es", "Python"]
caracter = input("Ingrese el carácter a contar: ")

conteo = {cadena: cadena.count(caracter) for cadena in lista_cadenas}

print("Frecuencia del carácter en cada cadena:", conteo)
