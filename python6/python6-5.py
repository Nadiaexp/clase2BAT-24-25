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

print("1 - Mostrar la suma de los dos números")
print("2 - Mostrar la resta del primero menos el segundo")
print("3 - Mostrar la multiplicación de los dos números")
print("4 - Salir del programa") 

o = int(input("Elija una de las 4 opciones: "))

while (o != 1) and (o != 2) and (o != 3) and (o != 4) :
    o = int(input("Elija una de las 4 opciones: "))

if (o == 1) :
    print(n + m)
elif (o == 2) :
    print(n - m)
elif (o == 3) :
    print(n * m)
elif (o == 4) :
    print("Fin del programa.")