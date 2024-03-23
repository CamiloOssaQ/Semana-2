# Definición de variables
entero = 10
flotante = 15.5
cadena = "Hola, mundo!"
lista = [1, 2, 3, 4, 5]
diccionario = {"nombre": "Juan", "edad": 30}

# Operaciones matemáticas
suma = entero + flotante
resta = flotante - entero
multiplicacion = entero * 2
division = flotante / 2

# Operaciones lógicas y comparativas
es_mayor = entero > flotante
es_igual = entero == 10
es_diferente = flotante != 10.0

# Estructura condicional (if, elif, else)
if es_mayor:
    print("El número entero es mayor que el número flotante.")
elif es_igual:
    print("El número entero es igual a 10.")
else:
    print("El número entero es menor que el número flotante.")

# Bucle for
print("Imprimiendo elementos de la lista:")
for elemento in lista:
    print(elemento)

# Bucle while
contador = 0
print("Contando hasta 5:")
while contador < 5:
    print(contador)
    contador += 1

# Imprimir datos por consola
print(f"La suma de {entero} y {flotante} es: {suma}")
print(f"La resta de {flotante} menos {entero} es: {resta}")
print(f"La multiplicación de {entero} por 2 es: {multiplicacion}")
print(f"La división de {flotante} entre 2 es: {division}")
print(f"¿{entero} es mayor que {flotante}? {es_mayor}")
print(f"¿{entero} es igual a 10? {es_igual}")
print(f"¿{flotante} es diferente de 10.0? {es_diferente}")
