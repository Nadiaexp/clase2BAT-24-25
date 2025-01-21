"""
Realiza un programa que lea dos números por teclado y permita elegir entre 4
opciones en un menú
1 - Mostrar la suma de los dos números
2 - Mostrar la resta de los dos números (el primero menos el segundo)
3 - Mostrar la multiplicación de los dos números
4 - Salir del programa
En caso de introducir una opción inválida, el programa volverá a solicitar otra
opción hasta que el usuario elija salir.

"""

n = int(input("Dime un número: "))
m = int(input("Dime otro número: "))

o = input("Elija una de las 4 opciones: ")

while (o != 1) or (o != 2) or (o != 3) or (o != 4) :
    print("Incorrecto, inténtalo de nuevo: ")

if (o == 1) :
    print("1 - Mostrar la suma de los dos números")

if (o == 2) :
    print("2 - Mostrar la resta del primero menos el segundo")

if (o == 3) :
    print("3 - Mostrar la multiplicación de los dos números")
    
if (o == 4) :
    print("4 - Salir del programa") 


    
