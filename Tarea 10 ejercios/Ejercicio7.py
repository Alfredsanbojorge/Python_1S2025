# Ejercicio 7: Dividir cada cadena en subcadenas usando un delimitador.

lista_cadenas = ["Hola mundo", "Python,es,genial", "Aprendiendo-Python"]
delimitador = input("Ingrese el delimitador para dividir las cadenas: ")

divididas = [cadena.split(delimitador) for cadena in lista_cadenas]

print("Cadenas divididas:", divididas)
