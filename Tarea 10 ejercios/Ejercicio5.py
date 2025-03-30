# Ejercicio 5: Reemplazar todas las apariciones de un carácter con otro.

lista_cadenas = ["Hola", "mundo", "esto", "es", "Python"]
caracter_antiguo = input("Ingrese el carácter a reemplazar: ")
caracter_nuevo = input("Ingrese el nuevo carácter: ")

cadenas_modificadas = [cadena.replace(caracter_antiguo, caracter_nuevo) for cadena in lista_cadenas]

print("Lista modificada:", cadenas_modificadas)
