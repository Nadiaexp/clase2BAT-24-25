"""
Crea un array con los número 10, 20, 30, 40 y 50 y luego muestra los que hay
en las posiciones impares (primero, tercero y quinto: 10, 30 y 50)

"""

datos = [10, 20, 30, 40, 50]

print("Imprimimos los impares: ")
for i in range(0,5):
    print(datos[datos // 2 != 0])
