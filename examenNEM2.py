"""
Realiza un programa que pida el día de la semana (del 1 al 7) y escriba
el día correspondiente. Si introducimos otro número nos da un error.
Nadia Expósito Moya
5/2/25

"""


n = int(input("Dime un número del 1 al 7: "))

if n == 1 :
    print("Lunes")
elif n == 2 : #Hacemos uso del "elif" para obtener valores al resto de números del 2 al 7.
    print("Martes")
elif n == 3 :
    print("Miércoles")
elif n == 4 :
    print("Jueves")
elif n == 5 :
    print("Viernes")
elif n == 6 :
    print("Sábado")
elif n == 7 :
    print("Domingo")
else : #Hacemos uso del "else" para dar el resultado de los números menores que 1 o mayores que 7.
    print("Ese día no existe :(")
