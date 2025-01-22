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

o = input("Elija una de las 4 opciones: ")

"""
while (o == 1) :
    o = float(input("1 - Mostrar la suma de los números"))
print(n + m)

while (o == 2) :
    o = float(input("2 - Mostrar la resta del primero menos el segundi"))
print(n - m)

while (o == 3) :
    o = float(input("3 - Mostrar la multiplicación de los dos números"))
print(n * m)

while (o == 4) :
    o = float(input("4 - Salir del programa"))
print("Apagado.")


while (o == 1 or 2 or 3 or 4) :
    
    if (o == 1) :
        print(n + m)
    if (o == 2) :
        print(n - m)
    if (o == 3) :
        print(n * m)
    if (o == 4) :
        print("Fin")

"""

while (o >= 1) or (o <= 4) :
    if o == 1 :
        print(n + m)
    if o == 2 :
        print(n - m)
    if o == 3 :
        print(n * m)
    if o == 4 :
        print("Fin")