"""
Escribe un programa que pida números hasta que se introduzca un cero.
Debe imprimir la suma de todos los números introducidos.
Nadia Expósito Moya
5/2/25

"""

#Damos los valores a la suma y a la x, siendo esta incógnita los distintos números que se van a recibir.
suma = 0
x = float(input("Dame un número: "))

while (x != 0) : 
    suma = suma + x
    x = float(input("Dame otro número: "))
print ("La suma es", suma) #Al dar un 0, se suman los números anteriores que se hayan dado.